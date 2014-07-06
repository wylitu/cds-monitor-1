# coding: utf-8
from mysql import connector
import time,datetime
import argparse
from mysql.connector import Error

class MysqlProcessCheck:

    def __init__(self,host,port,user,passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

    def check(self):
        alarm_msg=''
        value =0.0
        try:
            conn = connector.connect(user=self.user,password=self.passwd,database='information_schema',host=self.host,port=self.port)
            cursor = conn.cursor()
        except Exception, e:
            alarm_msg = '{}'.format(e)
            print("{\"monitorItem\":\"mysql_process_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":null}")
            return
        try:
            sql = "(select count(*) as process_num from processlist) union all (select count(*)   from information_schema.processlist  where user not in ('root')  and command not in ('Sleep', 'Connect', 'Binlog Dump')) "
            cursor.execute(sql)
            result = cursor.fetchall()
            value = result[1][0]*1.0/result[0][0]
        except Exception, e:
            conn.rollback()
            alarm_msg = '{}'.format(e)
        finally:
            cursor.close()
            conn.close()
        print("{\"monitorItem\":\"mysql_process_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":"+str(value)+"}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='db process check script')
    parser.add_argument('--h', help='the host of db')
    parser.add_argument('--p', help='the port of db', default=3306, type=int)
    #parser.add_argument('--n', help='the dbName of the db')
    parser.add_argument('--u', help='the user of the db')
    parser.add_argument('--pd', help='the password of the db')
    args = parser.parse_args()

    # 执行
    shell = MysqlProcessCheck(args.h,args.p,args.u,args.pd).check()


