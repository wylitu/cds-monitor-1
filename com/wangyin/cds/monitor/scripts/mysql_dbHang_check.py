# coding: utf-8
from mysql import connector
import time
import argparse
from mysql.connector import Error

class MysqlDbHangCheck:

    def __init__(self,host,port,dbName,user,passwd):
        self.host = host
        self.port = port
        self.dbName = dbName
        self.user = user
        self.passwd = passwd

    def check(self):
        alarm_msg=''
        try:
            conn = connector.connect(user=self.user,password=self.passwd,host=self.host,database=self.dbName,port=self.port)
            self.createHeartTable(conn)
            cursor = conn.cursor()
        except Exception, e:
            alarm_msg = "{}".format(e)
            print("{\"monitorItem\":\"mysql_dbHang_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":null}")
            return
        try:
            ISOTIMEFORMAT='%Y-%m-%d %X'
            date=time.strftime(ISOTIMEFORMAT, time.localtime())
            sql = "Update HA_HEARTBEAT  set HEARTBEAT ='"+date+"' where id=1234567"
            cursor.execute(sql)
            conn.commit()
        except Exception, e:
            conn.rollback()
            alarm_msg = 'update table `HA_HEARTBEAT` fails!{}'.format(e)
        finally:
            cursor.close()
            conn.close()
        print("{\"monitorItem\":\"mysql_dbHang_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":null}")

    def createHeartTable(self,conn):
         cursor = conn.cursor()
         sql = "SELECT count(*) FROM information_schema.tables WHERE table_schema ='"+self.dbName+"' AND table_name = 'HA_HEARTBEAT'"
         cursor.execute(sql)
         tablerows = cursor.fetchall()
         if tablerows[0][0]== 0:
             sql = 'CREATE TABLE `HA_HEARTBEAT` (`id` int(10) NOT NULL AUTO_INCREMENT,`HEARTBEAT`  DATETIME,PRIMARY KEY (`id`))ENGINE=InnoDB DEFAULT CHARSET=utf8'
             try:  
                 cursor.execute(sql)  
             except Exception,e:  
                 raise Exception, e
             insertSql = 'insert into `HA_HEARTBEAT` values(1234567,now())'
             try:  
                 cursor.execute(insertSql)
                 conn.commit()
             except Exception,e: 
                 conn.rollback()
                 raise Exception, e

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='db hang check script')
    parser.add_argument('--h', help='the host of db')
    parser.add_argument('--p', help='the port of db', default=3306, type=int)
    parser.add_argument('--n', help='the dbName of the db')
    parser.add_argument('--u', help='the user of the db')
    parser.add_argument('--pd', help='the password of the db')
    args = parser.parse_args()

    # 执行
    shell = MysqlDbHangCheck(args.h,args.p,args.n,args.u,args.pd).check()


