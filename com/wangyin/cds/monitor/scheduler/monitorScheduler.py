from apscheduler.scheduler import Scheduler
from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil

class MonitorScheduler:

    logger = LoggerUtil.getLogger('MonitorScheduler')
    def __init__(self):
        self.scheduler = Scheduler()

    def start(self):

    def stop(self):

    def err_listener(self,cls,event):
        if event.exception:
            cls.logger.exception('%s error.', str(event.job))
        else:  
            cls.logger.info('%s miss', str(event.job))

    def err_listener(self):
        self schedudler.add_listener(err_listener, apscheduler.events.EVENT_JOB_ERROR | apscheduler.events.EVENT_JOB_MISSED)


