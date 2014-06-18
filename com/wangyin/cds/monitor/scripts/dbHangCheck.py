# coding: utf-8
from connector import ClusterConnector
import time,datetime
from dbMonitorInstance import DbMonitorInstance
from dbMonitorInstance import MonitorIndexInstance
from mysql.connector import Error

class DbHangUtil:
    
    @staticmethod   
    def check(dbInfo,dbMonitor):
        print 'DbHangCheck[ip:'+dbInfo.getIp()+';port:'+dbInfo.getPort()+';dbName:'+dbInfo.getDbName()+'] start ...'
        dbMonitorInstance = None
        i=0
        while i<= dbMonitor.getRetryNum():
            if i> 0 :
                print 'The '+str(i)+' times few retries'
            conn = ClusterConnector().new_group_conn(dbInfo.getIp(),dbInfo.getPort(),dbInfo.getDbName())
            if conn!= None:
                break
            i= i+1
            time.sleep(5)
        if i > dbMonitor.getRetryNum():
            print 'db connect overtime [ip:'+dbInfo.getIp()+';port:'+dbInfo.getPort()+';dbName:'+dbInfo.getDbName()+']' 
            return DbMonitorInstance(dbMonitor.getGroupId(),dbMonitor.getMonitorItem(),dbMonitor.getMonitorItemName(),i,'db connect overtime')
         
        dbMonitorInstance = DbMonitorInstance(dbMonitor.getGroupId(),dbMonitor.getMonitorItem(),dbMonitor.getMonitorItemName(),i,'')
        monitorIndexConfigs = dbMonitor.getDbMonitorIndexs()
        if len(monitorIndexConfigs) == 0:
            return dbMonitorInstance
        DbHangUtil.createHeartTable(conn,dbInfo.getDbName())
        cursor = conn.cursor()
        for indexConfigs in monitorIndexConfigs:
             if indexConfigs.getIndexItem() == 'db_read':
                 print 'db_read check...'
                 try: 
                     startTime = datetime.datetime.now().microsecond
                     sql = "select HEARTBEAT from HA_HEARTBEAT where id=1234567"
                     cursor.execute(sql)
                     cursor.fetchall()
                     endTime = datetime.datetime.now().microsecond
                     timeDif = (endTime - startTime)/1000
                     dbMonitorIndexInstance = MonitorIndexInstance(indexConfigs.getIndexItem(),indexConfigs.getIndexItemName(),timeDif)
                     dbMonitorInstance.add_monitorIndexInstance(dbMonitorIndexInstance)
                 except Exception, e:  
                     print('query error!{}'.format(e))
                 print 'db_read check end'
             if indexConfigs.getIndexItem() == 'db_write':
                 print 'db_write check...'
                 try:
                     startTime = datetime.datetime.now().microsecond
                     ISOTIMEFORMAT='%Y-%m-%d %X'
                     date=time.strftime(ISOTIMEFORMAT, time.localtime())
                     sql = "Update HA_HEARTBEAT  set HEARTBEAT ='"+date+"' where id=1234567"
                     cursor.execute(sql)  
                     conn.commit()
                     endTime = datetime.datetime.now().microsecond
                     timeDif = (endTime - startTime)/1000
                     dbMonitorIndexInstance = MonitorIndexInstance(indexConfigs.getIndexItem(),indexConfigs.getIndexItemName(),timeDif)
                     dbMonitorInstance.add_monitorIndexInstance(dbMonitorIndexInstance)
                 except Exception, e:  
                     conn.rollback()
                     print('update error!{}'.format(e))
                 print 'db_write check end'  
        cursor.close()  
        conn.close()
        return dbMonitorInstance

    @staticmethod 
    def createHeartTable(conn,dbName):
         cursor = conn.cursor()
         sql = "SELECT count(*) FROM information_schema.tables WHERE table_schema ='"+dbName+"' AND table_name = 'HA_HEARTBEAT'"
         cursor.execute(sql)
         tablerows = cursor.fetchall()
         if tablerows[0][0]== 0:
             sql = 'CREATE TABLE `HA_HEARTBEAT` (`id` int(10) NOT NULL AUTO_INCREMENT,`HEARTBEAT`  DATETIME,PRIMARY KEY (`id`))ENGINE=MyISAM DEFAULT CHARSET=utf8'  
             try:  
                 cursor.execute(sql)  
             except Exception,e:  
                 print('create table `HA_HEARTBEAT` fails!{}'.format(e))  

             insertSql = 'insert into `HA_HEARTBEAT` values(1234567,now())'
             try:  
                 cursor.execute(insertSql)
                 conn.commit()
             except Exception,e: 
                 conn.rollback()
                 print('insert table `HA_HEARTBEAT` fails!{}'.format(e))  

             

useradd -s /bin/bash -g group ¨CG root bingyi
useradd ¨Cb /home/david -m david
         


