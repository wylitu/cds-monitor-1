
from apscheduler.scheduler import Scheduler
#from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil
from com.wangyin.cds.monitor.utils.cdsUtil import CDSUtil
from com.wangyin.cds.monitor.scheduler.monitorTask import MonitorTask
from com.wangyin.cds.monitor.utils.configUtil  import ConfigUtil
import time

class MonitorScheduler:

    #logger = LoggerUtil.getLogger('MonitorScheduler')

    def __init__(self,events):
        self.scheduler = Scheduler(daemonic = False)
        self.events = events
        self.flag = False
        self.runflag = True
        if self.events !=None:
            self.flag = True

    def monitorListener(self):
         print self.events
         if self.flag == True:
            self.monitor_task_start(self.events)
            flag = False
         else:
             events = self.event_filter(CDSUtil.getEvents(CDSUtil))
             self.monitor_task_start(events)

    def start(self):
        print('MonitorScheduler start ...')
        while self.runflag:
            try:
                self.monitorListener()
            except Exception as e:
                print(e)
            time.sleep(60)
        #self.scheduler.add_interval_job('monitorListener',seconds=5)
        #self.scheduler.start()
    def stop(self):
         self.runflag = False


    # Filtering duplicate events
    def event_filter(self,events):
        eventInfos = []
        if events == None:
            return None
        for event in events:
             eventId = ConfigUtil().getEventId(event.getMonitorId())
             if event.getEventId() != eventId:
                 eventInfos.append(event)
        ConfigUtil().setEvents(eventInfos)
        return eventInfos

    def monitor_task_start(self,events):
         if events == None:
            return
         for event in events:
              MonitorTask(event).start()

    def err_listener(self,cls,event):
        if event.exception:
            cls.logger.exception('%s error.', str(event.job))
        else:  
            cls.logger.info('%s miss', str(event.job))

    def err_listener(self):
        self.scheduler.add_listener(self.err_listener, self.apscheduler.events.EVENT_JOB_ERROR | self.apscheduler.events.EVENT_JOB_MISSED)


