from apscheduler.scheduler import Scheduler
from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil
from com.wangyin.cds.monitor.utils.cdsUtil import CDSUtil
from concurrent.futures import ProcessPoolExecutor


class MonitorScheduler:

    logger = LoggerUtil.getLogger('MonitorScheduler')
    def __init__(self,dbConfig,dbMonitorConfig):
        self.scheduler = Scheduler(daemonic = False)
        self.scheduler.cron_schedule(second='*', day_of_week='0-4', hour='9-12,13-15', jobstore='monitorListener')
        self.dbConfig = dbConfig
        self.dbMonitorConfig = dbMonitorConfig
    def start(self):
        self.scheduler.start()
    def stop(self):
         self.scheduler._stopped()
    def monitorListener(self):
         return

    def err_listener(self,cls,event):
        if event.exception:
            cls.logger.exception('%s error.', str(event.job))
        else:  
            cls.logger.info('%s miss', str(event.job))

    def err_listener(self):
        self.scheduler.add_listener(self.err_listener, self.apscheduler.events.EVENT_JOB_ERROR | self.apscheduler.events.EVENT_JOB_MISSED)


