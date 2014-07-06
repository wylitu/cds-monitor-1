#from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil
import subprocess
from com.wangyin.cds.monitor.model.dbInfo import DbConfig
from com.wangyin.cds.monitor.model.dbMonitor import DbMonitorConfig
from com.wangyin.cds.monitor.model.dbMonitorInstance import DbMonitorInstance
from com.wangyin.cds.monitor.utils.cdsUtil import CDSUtil
from com.wangyin.cds.monitor.utils.configUtil import ConfigUtil
import time,json
class MonitorCollector:

    #logger = LoggerUtil.getLogger('MonitorCollector')

    #def __init__(self):
    #    self.dbConfig=None
    #    self.dbMonitor=None
    def __init__(self,dbConfig,dbMonitor):
        self.dbConfig = dbConfig
        self.dbMonitor = dbMonitor
        self.retry_num = self.dbMonitor.retry_num
        self.cmd =''

    def start(self):
        print 'MonitorCollector start'
        check_interval = self.dbMonitor.check_interval
        scriptPath = self.dbMonitor.scriptPath
        db_info_id = self.dbConfig.db_info_id
        dbUnit = self.dbConfig.db_units[0]
        reMsg = None
        errorMsg = None
        if self.dbMonitor.monitor_type == 'HOST':
            self.cmd = "python ../scripts/"+scriptPath
        else:
            if self.dbMonitor.monitor_item == 'mysql_dbHang_check' or self.dbMonitor.monitor_item == 'ora_dbHang_check':
                self.cmd = "python ../scripts/"+scriptPath+" --h "+dbUnit.ip+" --p "+str(dbUnit.port)+" --n " \
                                +dbUnit.db_name+" --u "+dbUnit.user_name+" --pd "+dbUnit.passwd
            else:
                self.cmd = "python ../scripts/"+scriptPath+" --h "+self.dbConfig.ip+" --p "+str(self.dbConfig.port) \
                                +" --u "+self.dbConfig.user_name+" --pd "+self.dbConfig.passwd
        print self.cmd
        i=0
        while i<= self.retry_num:
             p=subprocess.Popen(self.cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
             j = 0
             while j<1:
                 buff = p.stdout.readline()
                 j = j + 1
             print buff
             reMsg = json.loads(buff.replace('\n',''))
             if reMsg['monitorItem'] != self.dbMonitor.monitor_item:
                 errorMsg = 'monitor scripts and monitor item does not match'
                 break
             if reMsg['alarmMsg'] == None or reMsg['alarmMsg'] == '':
                 CDSUtil.sendMonitorInstance(CDSUtil,DbMonitorInstance(self.dbMonitor.id,db_info_id,self.dbMonitor.monitor_item
                                                                      ,int(time.time()*1000),i,reMsg['monitorValue'], '',self.dbMonitor.monitor_type,self.dbMonitor.unit))
                 i=0
             else:
                 errorMsg =  reMsg['alarmMsg']
                 i = i+1
                 continue
             time.sleep(check_interval)
        ConfigUtil().setEvents(self.events)
        CDSUtil.sendMonitorInstance(CDSUtil,DbMonitorInstance(self.dbMonitor.id,db_info_id,self.dbMonitor.monitor_item,int(time.time()*1000)
                                                              ,self.retry_num+1, '',errorMsg,self.dbMonitor.monitor_type,self.dbMonitor.unit))
    def stop(self):
         self.retry_num = -1

#if __name__ == '__main__':
    #MonitorCollector().start()