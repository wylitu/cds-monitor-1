#from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil
#from concurrent.futures import ProcessPoolExecutor
from com.wangyin.cds.monitor.utils.scriptLoad import ScriptLoad
from com.wangyin.cds.monitor.utils.cdsUtil import CDSUtil
from com.wangyin.cds.monitor.scheduler.monitorCollector import MonitorCollector
import multiprocessing
class MonitorTaskProcess(multiprocessing.Process):

    #logger = LoggerUtil.getLogger('MonitorTask')

    def __init__(self,event):
         super(MonitorTaskProcess, self).__init__()
         self.event = event
         host = self.event.dbConfig.ip
         db_type = self.event.dbConfig.db_type
         dbConfig = self.event.dbConfig
         dbConfig.db_units =  CDSUtil.get_db_unit(CDSUtil,host,db_type)
         self.dbMonitor = CDSUtil.getDbMonitorConfigByDbMonitorId(CDSUtil,self.event.monitorId)
         self.monitorCollector =MonitorCollector(dbConfig,self.dbMonitor)

    def run(self):
         print 'load script'
         ScriptLoad().load(self.dbMonitor.scriptPath)
         self.monitorCollector.start()
    def stop(self):
         self.monitorCollector.stop()


#if __name__ == '__main__':
#     MonitorTask(None).start()