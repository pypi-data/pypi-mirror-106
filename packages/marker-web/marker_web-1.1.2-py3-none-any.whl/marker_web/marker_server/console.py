import asyncio

from marker.utils.console import ConsoleABC
from marker.utils.token import TokenNotFoundError
from .jobs import JobTracker

class WebConsole(ConsoleABC):
    
    def error(self, *args, **kwargs):
        print(f'[-]', *args)
        JobTracker.addMessage('ERR: ' + " ".join(map(str,args)))
        JobTracker.errors = True

    def log(self, *args, **kwargs):
        JobTracker.addMessage('LOG: ' + " ".join(map(str,args)))
    
    # No input from webserver
    def get(self, prompt, **kwargs):
        return None

    def ask(self, prompt, default=False):
        return default
    
    def track(self, tasks, label="Processing"):
        JobTracker.setTotal(len(tasks))
        for task in tasks:
            yield task
            JobTracker.updateProgress(1)
            if JobTracker.shouldExitNow:
                JobTracker.threadExit()
        JobTracker.finishJob()

    async def track_async(self, tasks, label="Processing"):
        JobTracker.setTotal(len(tasks))
        results = []
        for task in asyncio.as_completed(tasks):
            try:
                result = await task
                results.append(result)
            except TokenNotFoundError:
                raise
            except Exception as e:
                self.error("Exception occured:", e)

            JobTracker.updateProgress(1)
            if JobTracker.shouldExitNow:
                JobTracker.threadExit()
        JobTracker.finishJob()
        return results