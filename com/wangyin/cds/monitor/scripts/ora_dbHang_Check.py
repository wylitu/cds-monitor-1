# coding: utf-8
from com.wangyin.cds.monitor.utils.connector import DbConnector
import time,datetime
from mysql.connector import Error

class DbHangCheck:

    def check(self,dbInfo,dbMonitor):
        return
    def createHeartTable(self,conn,dbName):
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

    def start(self):
         return

    if __name__ == '__main__':
        start()



