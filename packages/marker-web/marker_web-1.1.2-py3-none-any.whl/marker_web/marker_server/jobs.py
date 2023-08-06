import json
from flask import make_response
from marker import TokenNotFoundError
import threading 
import sys

class JobTracker:
    name = "No jobs added yet."
    progress = 100
    total = 100
    done = True
    errors = False
    logs = ""
    killed = False
    jobType = "none"

    # Threads will check this to see if they
    # Should stop processing and exit.
    shouldExitNow = False

    @staticmethod
    def isBusy():
        return JobTracker.done == False

    @staticmethod
    def setJob(name, jobType):
        if JobTracker.isBusy():
            return False
        JobTracker.name = name
        JobTracker.progress = 0
        JobTracker.total = 100
        JobTracker.done = False
        JobTracker.errors = False
        JobTracker.killed = False
        JobTracker.logs = ""
        JobTracker.jobType = jobType
        JobTracker.tokenMissing = False
    
    @staticmethod
    def getInfo():
        if JobTracker.tokenMissing:
            raise TokenNotFoundError("Could not find token")
        info = { 
            'name': JobTracker.name,
            'progress': JobTracker.progress,
            'total': JobTracker.total,
            'done': JobTracker.done,
            'errors': JobTracker.errors,
            'logs': JobTracker.logs,
            'killed': JobTracker.killed,
            'type': JobTracker.jobType
        }
        return info
    
    @staticmethod
    def setTotal(total):
        JobTracker.total = total
    
    @staticmethod
    def updateProgress(inc=1):
        JobTracker.progress += inc

    @staticmethod
    def finishJob():
        JobTracker.done = True
        JobTracker.progress = JobTracker.total
        JobTracker.shouldExitNow = False
        print(f"[+] Job `{JobTracker.name}` finished")

    @staticmethod
    def addMessage(msg):
        JobTracker.logs += msg + "\n"
        
    @staticmethod
    def runSync(func):
        if JobTracker.isBusy():
            raise Exception("busy")

        JobTracker.setJob("Processing", "sync")

        try:
            ret = func()
        finally:
            JobTracker.finishJob()
        
        if JobTracker.errors:
            raise Exception(JobTracker.logs)

        return ret
    
    @staticmethod
    def runAsync(func, label="Processing...", jobType=""):
        if JobTracker.isBusy():
            raise Exception("busy")

        # Make an auxiliary function that always runs `finishJob`
        def wrapper():
            try:
                func()
            except BaseException as e:
                JobTracker.logs += str(e)
                JobTracker.killed = True
                if isinstance(e, TokenNotFoundError):
                    JobTracker.tokenMissing = True
            finally:
                JobTracker.finishJob()
        
        # Reset old values before starting...
        JobTracker.setJob(label, jobType)
        threading.Thread(target=wrapper).start()
        return make_response("Job started!", 200)

    @staticmethod
    def setStop():
        if (JobTracker.isBusy()):
            JobTracker.shouldExitNow = True

        # Got request to stop, but no job running.
        else:
            pass

    @staticmethod
    def threadExit():
        JobTracker.addMessage("STOP: The job was stopped")
        JobTracker.killed = True
        JobTracker.total = 0
        JobTracker.finishJob()
        # Kill the thread...
        sys.exit()
