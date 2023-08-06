from concurrent.futures import ThreadPoolExecutor, wait, Future
import threading
import sys
from pprint import pformat
from pysquid import stream_logger
from pysquid.plugin import Hook
from pysquid.core import _ID_TASK


def setup_thread_excepthook():
    """
    Workaround for sys.excepthook bug
    """

    init_orginal = threading.Thread.__init__

    def init(self, *args, **kwargs):

        init_orginal(self, *args, **kwargs)
        run_original = self.run

        def run_with_except_hook(*args2, **kwargs2):
            try:
                run_original(*args2, **kwargs2)

            except Exception:
                sys.excepthook(*sys.exc_info())

        self.run = run_with_except_hook

    threading.Thread.__init__ = init
    

class ThreadedEngine():

    def __init__(self, template, plugins, except_hook=None, log=None, max_workers=50, max_pool_workers=20):
        self.template = template
        self.plugins = plugins
        self.log = log if log else stream_logger()
        self.max_workers = max_workers
        self.max_pool_workers = max_pool_workers
        setup_thread_excepthook()
        sys.excepthook = except_hook if except_hook else self.inbuilt_except_hook
        self.exceptions = []
        self.pools = {}

    def inbuilt_except_hook(self, exctype, value, tb):
        """
        Catch exceptions
        """
        self.log.info(f'Exception: {exctype}, {value}')
        self.exceptions.append({'type': exctype})
        
    def build(self):

        services = self.template.get(_ID_TASK)
        plugins = self.plugins
        
        pools = {
            'thread': {}
        }

        playbook = {}

        for sid, service in services.items():

            mode = service.get('__mode__')
            plugin = service.get('__plugin__')
            workers = service.get('__workers__')

            if mode not in pools or plugin not in plugins:
                continue

            enabled_workers = set(workers.keys())

            plugin_ = plugins.get(plugin)()
            plugin_.add_service(service, self.template)

            setup = plugin_.iterate_workers(enabled_workers)

            for pid, stages in setup.items():
                if pid not in playbook:
                    playbook[pid] = {}
                    
                for sid, stage in stages.items():
                    if sid not in playbook[pid]:
                        playbook[pid][sid] = []

                    playbook[pid][sid] = playbook[pid][sid] + setup[pid][sid] 

        pools['thread'] = playbook
        self.pools = pools
        
    def exec_pool(self, hook: Hook = None):

        pools = self.pools.get('thread')        
        futures = set()

        hook = hook if isinstance(hook, Hook) else Hook()

        exception_count = 0
        
        for pid, pool in pools.items():
            self.log.info(f'Running pool {pid}')
            e = ThreadPoolExecutor(max_workers=self.max_pool_workers)

            try:            
                future = e.submit(self.exec_workers, pool, hook)

                if isinstance(future, Future):
                    futures.add(future)

            except Exception as _e:
                self.log.info(f'Error submitting pool: {_e!r}')

        self.log.info(f'Waiting on {futures}')
        wait(futures)

        for finished_worker in futures:
            self.log.debug(pformat(finished_worker.__dict__))
            exception_count += finished_worker._result
            
        self.log.info(f'Future done: {futures}, exceptions: {exception_count}')

        return exception_count
            
    def exec_workers(self, pool, hook):

        e = ThreadPoolExecutor(max_workers=self.max_workers)
        futures = set()

        pipeline = dict(sorted(pool.items(), key=lambda item: item[0]))

        exceptions = 0
        
        for sid, stage in pipeline.items():
            
            for worker in stage:
                # Set worker and run init

                try:
                    hook.set_worker(worker)
                    hook.init()                
                    worker.pre()
                    future = e.submit(worker.apply)

                    if isinstance(future, Future):
                        futures.add(future)

                except Exception as _e:
                    self.log.info(f'Error submitting worker: {_e!r}')

            wait(futures)

            for finished_worker in futures:
                self.log.debug(pformat(finished_worker.__dict__))

                if finished_worker._exception:
                    exceptions += 1
                    
            for worker in stage:

                try:                
                    worker.post()
                    hook.set_worker(worker)
                    hook.cleanup()

                except Exception as _e:
                    self.log.info(f'Error submitting worker: {_e!r}')
                
        return exceptions
    


