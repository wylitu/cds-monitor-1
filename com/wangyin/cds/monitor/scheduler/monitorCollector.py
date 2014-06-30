#from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil
import subprocess
from com.wangyin.cds.monitor.model.dbInfo import DbConfig
from com.wangyin.cds.monitor.model.dbMonitor import DbMonitorConfig
from com.wangyin.cds.monitor.model.dbMonitorInstance import DbMonitorInstance
from com.wangyin.cds.monitor.utils.cdsUtil import CDSUtil
import datetime
class MonitorCollector:

    #logger = LoggerUtil.getLogger('MonitorCollector')

    #def __init__(self):
    #    self.dbConfig=None
    #    self.dbMonitor=None
    def __init__(self,dbConfig,dbMonitor):
        self.dbConfig = dbConfig
        self.dbMonitor = dbMonitor
        self.retry_num = self.dbMonitor.retry_num

    def start(self):
        check_interval = self.dbMonitor.check_interval
        scriptPath = self.dbMonitor.scriptPath
        dbUnit = self.dbConfig.db_units[0]
        errorMsg = ''
        i=0
        while i<= self.retry_num:
             p=subprocess.Popen("python ../scripts/"+scriptPath+" --h "+dbUnit.ip+" --p "+str(dbUnit.port)+" --n " \
                                +dbUnit.db_name+" --u "+dbUnit.user_name+" --pd "+dbUnit.passwd,
                           shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
             while True:
                 buff = p.stdout.readline()
                 print buff
                 if buff == '' and p.poll() != None:
                     break
             errorMsg = buff
             if buff == None:
                 CDSUtil.sendMonitorInstance(CDSUtil,DbMonitorInstance(self.dbMonitor.id,self.dbMonitor.monitor_item,datetime.datetime.now().microsecond,i, '',''))
                 i=0
             else:
                 i = i+1
        CDSUtil.sendMonitorInstance(CDSUtil,DbMonitorInstance(self.dbMonitor.id,self.dbMonitor.monitor_item,datetime.datetime.now().microsecond,self.retry_num+1, '',errorMsg))
    def stop(self):
         self.retry_num = -1

#if __name__ == '__main__':
    #MonitorCollector().start()