# coding: utf-8
from mysql import connector
import time,datetime
import argparse
from mysql.connector import Error

class MysqlDataSpaceCheck:

    def __init__(self,host,port,user,passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.monitor_sql = 'select sum(max_data_length) max_data_length, sum(data_length) data_length from tables'
    def check(self):
        alarm_msg=''
        value =None
        try:
            conn = connector.connect(user=self.user,password=self.passwd,database='information_schema',host=self.host,port=self.port)
            cursor = conn.cursor()
        except Exception, e:
            alarm_msg = '{}'.format(e)
            print("{\"monitorItem\":\"mysql_dataSpace_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":null}")
            return
        try:
            cursor.execute(self.monitor_sql)
            result = cursor.fetchall()
            if result:
                max_data_length, data_length = result[0][0], result[0][1]
                if max_data_length and data_length:
                    value = float(data_length)/float(max_data_length)*100
                    value = float('%.2f' % value)
            else:
                 alarm_msg ='cant check result is null'
        except Exception, e:
            conn.rollback()
            alarm_msg = '{}'.format(e)
        finally:
            cursor.close()
            conn.close()
        result_info = "{\"monitorItem\":\"mysql_dataSpace_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":"
        if value ==None:
            result_info = result_info.__add__("null}")
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
    shell = MysqlDataSpaceCheck(args.h,args.p,args.u,args.pd).check()


