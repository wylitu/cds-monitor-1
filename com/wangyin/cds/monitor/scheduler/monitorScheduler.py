
from apscheduler.scheduler import Scheduler
#from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil
from com.wangyin.cds.monitor.utils.cdsUtil import CDSUtil
from com.wangyin.cds.monitor.scheduler.monitorTaskProcess import MonitorTaskProcess
from com.wangyin.cds.monitor.utils.configUtil  import ConfigUtil
from concurrent.futures import ProcessPoolExecutor as Executer
import time,multiprocessing

class MonitorScheduler:

    #logger = LoggerUtil.getLogger('MonitorScheduler')

    def __init__(self,events):
        self.scheduler = Scheduler(daemonic = False)
        self.scheduler.add_cron_job(self.monitorListener, second='*/3')
        self.events = events
        self.flag = True
        self.runflag = True
        if self.events !=None:
            self.flag = True
        self.monitor_tasks = {}

    def monitorListener(self):
         if self.flag == True:
             print "first monitorListener:"
             self.flag = False
             ConfigUtil().setEvents(self.events)
             self.monitor_tasks_start(self.events)
         else:
             events = CDSUtil.getEvents(CDSUtil)
             eventInfos = self.event_filter(events)
             if eventInfos == None or len(eventInfos) == 0:
                 return
             ConfigUtil().setEvents(events)
             self.monitor_tasks_start(eventInfos)

    def start(self):
        print('MonitorScheduler start ...')
        self.scheduler.start()

    def stop(self):
         self.scheduler._stopped()

    # Filtering duplicate events
    def event_filter(self,events):
        eventInfos = []
        if events == None or len(events) == 0:
            return None
        for event in events:
             if ConfigUtil().is_config_has_event(event) == False:
                 eventInfos.append(event)
        return eventInfos

    def monitor_task_start(self,monitorTask):
        monitorTask.start()

    def monitor_tasks_start(self,events):
         if events == None and len(events) == 0:
             return
         for event in events:
             monitorTask = self.monitor_tasks.get(str(event.monitorId)+'_'+str(event.dbConfig.db_info_id))
             print event.monitorId
             if event.eventType == None:
                 break
             if event.eventType == 'MONITOR_START':
                 if monitorTask:
                     monitorTask.stop()
                 print 'save start ...'
                 monitorTask = MonitorTaskProcess(event)
                 self.monitor_tasks[str(event.monitorId)+'_'+str(event.dbConfig.db_info_id)] = monitorTask
                 print(self.monitor_tasks)

                 try:
                    monitorTask.start()
                    print 'save end ...'
                 except Exception as e:
                     print(e)
             else:
                 if monitorTask:
                     monitorTask.stop()
                     monitorTask.terminate()
                     self.monitor_tasks[str(event.monitorId)+'_'+str(event.dbConfig.db_info_id)] = None


    def err_listener(self,cls,event):
        if event.exception:
            cls.logger.exception('%s error.', str(event.job))
        else:
            cls.logger.info('%s miss', str(event.job))

    def err_listener(self):
        self.scheduler.add_listener(self.err_listener, self.apscheduler.events.EVENT_JOB_ERROR | self.apscheduler.events.EVENT_JOB_MISSED)

#if __name__ == '__main__':
 #   MonitorTaskProcess(None).start()

