# coding: utf-8
import os
from dbMonitorInstance import DbMonitorInstance
class PingUtil:
    @staticmethod   
    def check(dbInfo,dbMonitor):
        print 'pingCheck[ip:'+dbInfo.getIp()+';port:'+dbInfo.getPort()+';dbName:'+dbInfo.getDbName()+'] start ...'
        dbMonitorInstance = None
        i=0
        msg = ''
        while i<= dbMonitor.getRetryNum():
            if i> 0 :
                print 'The '+str(i)+' times few retries'
            data = os.system('ping  '+dbInfo.getIp())
            if data==0:
               break
            else:
               i= i+1
        if i > dbMonitor.getRetryNum():
            msg ='connect server gatway overtime'  
            print 'connect server gatway overtime [ip:'+dbInfo.getIp()+';dbGroupId:'+dbInfo.groupId()+']' 
        return DbMonitorInstance(dbMonitor.getGroupId(),dbMonitor.getMonitorItem(),dbMonitor.getMonitorItemName(),i,msg)



    if __name__ == '__main__':
        main()



