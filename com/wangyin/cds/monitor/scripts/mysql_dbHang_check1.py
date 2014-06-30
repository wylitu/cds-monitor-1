# coding: utf-8
from mysql import connector
import time,datetime
import argparse
from mysql.connector import Error

class MysqlDbHangCheck:
    
    @staticmethod   
    def check(cls,host,port,dbName,user,passwd):

        try:
            conn = connector.connect(user=user,password=passwd,host=host,database=dbName,port=port)
            cls.createHeartTable(conn,dbName)
            cursor = conn.cursor()
        except Exception, e:
            print e
            return
        try:
            ISOTIMEFORMAT='%Y-%m-%d %X'
            date=time.strftime(ISOTIMEFORMAT, time.localtime())
            sql = "Update HA_HEARTBEAT  set HEARTBEAT ='"+date+"' where id=1234567"
            cursor.execute(sql)
            conn.commit()
        except Exception, e:
            conn.rollback()
            print('update table `HA_HEARTBEAT` fails!{}'.format(e))
        finally:
            cursor.close()
            conn.close()
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
                 return
             insertSql = 'insert into `HA_HEARTBEAT` values(1234567,now())'
             try:  
                 cursor.execute(insertSql)
                 conn.commit()
             except Exception,e: 
                 conn.rollback()
                 print('insert table `HA_HEARTBEAT` fails!{}'.format(e))  

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='db hang check script')
    parser.add_argument('--h', help='the host of db', default='192.168.1.102')
    parser.add_argument('--p', help='the port of db', default=3306, type=int)
    parser.add_argument('--n', help='the dbName of the db')
    parser.add_argument('--u', help='the user of the db')
    parser.add_argument('--pd', help='the password of the db')
    args = parser.parse_args()

    # 执行
    shell = MysqlDbHangCheck.check(MysqlDbHangCheck,args.h,args.p,args.n,args.u,args.pd)


