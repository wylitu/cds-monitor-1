# coding: utf-8
from mysql import connector
import time,datetime
import argparse
from mysql.connector import Error

class MysqlStandbyCheck:

    def __init__(self,host,port,user,passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.monitor_sql = 'show slave status'
    def check(self):
        alarm_msg=''
        value =None
        try:
            conn = connector.connect(user=self.user,password=self.passwd,host=self.host,port=self.port)
            cursor = conn.cursor()
        except Exception, e:
            alarm_msg = e.message
            print("{monitorItem:'mysql_standby_check',alarmMsg:'"+alarm_msg+"',monitorValue:}")
            return
        try:
            cursor.execute(self.monitor_sql)
            result = cursor.fetchall()
            if result:
                Seconds_Behind_Master, Slave_IO_Running, Slave_SQL_Running = result[0]['Seconds_Behind_Master'], result[0]['Slave_IO_Running'], result[0]['Slave_SQL_Running']
                if Slave_IO_Running == 'Yes' and Slave_SQL_Running == 'Yes':
                    if Seconds_Behind_Master:
                        value = float(Seconds_Behind_Master)
                elif Slave_IO_Running == 'No':
                    alarm_msg ='Slave_IO_Running is no'
                elif Slave_SQL_Running == 'No':
                    alarm_msg ='Slave_SQL_Running is no'
            else:
                 alarm_msg ='slave sync is not start'
        except Exception, e:
            conn.rollback()
            alarm_msg = e.message
        finally:
            cursor.close()
            conn.close()
        result_info = "{monitorItem:'mysql_standby_check',alarmMsg:'"+alarm_msg+"',monitorValue:"
        if value ==None:
            result_info = result_info.__add__("}")
        else:
            result_info = result_info.__add__(str(value)+"}")
        print(result_info)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='db process check script')
    parser.add_argument('--h', help='the host of db')
    parser.add_argument('--p', help='the port of db', default=3306, type=int)
    #parser.add_argument('--n', help='the dbName of the db')
    parser.add_argument('--u', help='the user of the db')
    parser.add_argument('--pd', help='the password of the db')
    args = parser.parse_args()

    # 执行
    shell = MysqlStandbyCheck(args.h,args.p,args.u,args.pd).check()


