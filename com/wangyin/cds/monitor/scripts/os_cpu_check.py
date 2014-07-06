__author__ = 'wylitu'
# coding: utf-8
import argparse
import subprocess

class OsCpuCheck:

    def check(self):
        alarm_msg = ''
        try:
            p=subprocess.Popen("mpstat| grep all| awk '{print $4}'",shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except Exception as e:
            alarm_msg = "{}".format(e)
            print("{\"monitorItem\":\"os_cpu_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":null}")
            return
        while True:
            msg = p.stdout.readline()
            if msg != '':
                break
        print("{\"monitorItem\":\"os_cpu_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":"+msg.replace(' ','').replace('\n','')+"}")

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='db hang check script')
   # parser.add_argument('--h', help='the host of db', default='192.168.1.102')
    #parser.add_argument('--p', help='the port of db', default=3306, type=int)
    #parser.add_argument('--n', help='the dbName of the db')
   # parser.add_argument('--u', help='the user of the db')
   # parser.add_argument('--pd', help='the password of the db')
    #args = parser.parse_args()

    # 执行
    shell = OsCpuCheck().check()


