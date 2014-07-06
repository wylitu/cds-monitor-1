# coding: utf-8
from mysql import connector
import datetime,time
import argparse
from mysql.connector import Error

class MysqlIopsCheck:

    def __init__(self,host,port,user,passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.monitor_value_dict = {}
        self.first_flag = True
        self.monitor_value_name_list = ('Innodb_data_writes', 'Innodb_data_reads')
        for value_name in self.monitor_value_name_list:
            self.monitor_value_dict[value_name] = [None,
             None,
             None,
             None]

    def monitor_value(self, monitor_value):
        tmp_value = {}
        for row in monitor_value:
            if row[0] in self.monitor_value_name_list:
                tmp_value[row[0]] = float(row[1])

        else:
            if len(tmp_value) != len(self.monitor_value_name_list):
                raise Exception, 'can not get all value (%s),(%s)' % (tmp_value.keys(), self.monitor_value_name_list)
        for value_name in tmp_value.keys():
            self.monitor_value_dict[value_name][2] = tmp_value[value_name]
            self.monitor_value_dict[value_name][3] = datetime.datetime.now()

        innodb_iops = 0
        if self.first_flag:
            for value_name in tmp_value.keys():
                self.monitor_value_dict[value_name][0] = self.monitor_value_dict[value_name][2]
                self.monitor_value_dict[value_name][1] = self.monitor_value_dict[value_name][3]
            else:
                self.first_flag = False

        else:
            tmp_Innodb_data_writes = self.monitor_value_dict['Innodb_data_writes'][2] - self.monitor_value_dict['Innodb_data_writes'][0]
            tmp_Innodb_data_read = self.monitor_value_dict['Innodb_data_reads'][2] - self.monitor_value_dict['Innodb_data_reads'][0]
            time_elapse = (self.monitor_value_dict['Innodb_data_writes'][3] - self.monitor_value_dict['Innodb_data_writes'][1]).total_seconds()
            innodb_iops = (tmp_Innodb_data_writes + tmp_Innodb_data_read) / time_elapse
            for value_name in tmp_value.keys():
                self.monitor_value_dict[value_name][0] = self.monitor_value_dict[value_name][2]
                self.monitor_value_dict[value_name][1] = self.monitor_value_dict[value_name][3]

        innodb_iops = float('%.2f' % innodb_iops)
        return innodb_iops
    def check(self):
        alarm_msg=''
        value =0.0
        dataWrites =''
        dataRead =''
        try:
            conn = connector.connect(user=self.user,password=self.passwd,host=self.host,port=self.port)
            cursor = conn.cursor()
        except Exception, e:
            alarm_msg = '{}'.format(e)
            print("{\"monitorItem\":\"mysql_iops_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":null}")
            return
        try:
            i=0
            while i<2:
                sql = "show global status like 'Innodb_data%'"
                cursor.execute(sql)
                result = cursor.fetchall()
                value = self.monitor_value(result)
                i = i +1
                time.sleep(1);

        except Exception, e:
            conn.rollback()
            alarm_msg = '{}'.format(e)
        finally:
            cursor.close()
            conn.close()
        print("{\"monitorItem\":\"mysql_iops_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":"+str(value)+"}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='db process check script')
    parser.add_argument('--h', help='the host of db')
    parser.add_argument('--p', help='the port of db', default=3306, type=int)
    #parser.add_argument('--n', help='the dbName of the db')
    parser.add_argument('--u', help='the user of the db')
    parser.add_argument('--pd', help='the password of the db')
    args = parser.parse_args()

    # 执行
    shell = MysqlIopsCheck(args.h,args.p,args.u,args.pd).check()


