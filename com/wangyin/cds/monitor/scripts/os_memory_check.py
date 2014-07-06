__author__ = 'wylitu'
# coding: utf-8
import argparse
import subprocess

class OsMemoryCheck:

    def check(self):
        alarm_msg = ''
        try:
            p=subprocess.Popen("cat /proc/meminfo | awk '{print $1$2}'",shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except Exception as e:
            alarm_msg = "{}".format(e)
            print("{\"monitorItem\":\"os_memory_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":null}")
            return
        i=0
        memTotal = 0
        memFree=0
        buffers=0
        cached=0
        while i<4:
            msg = p.stdout.readline()
            if i == 0:
                memTotal = msg.split(':')[1].strip()
            if i == 1:
                memFree = msg.split(':')[1].strip()
            if i == 2:
                buffers = msg.split(':')[1].strip()
            if i == 3:
                cached = msg.split(':')[1].strip()

        value = (memTotal - memFree - buffers - cached)*1.0/memTotal
        print("{\"monitorItem\":\"os_memory_check\",\"alarmMsg\":\""+alarm_msg+"\",\"monitorValue\":"+value+"}")

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='db hang check script')
   # parser.add_argument('--h', help='the host of db', default='192.168.1.102')
    #parser.add_argument('--p', help='the port of db', default=3306, type=int)
    #parser.add_argument('--n', help='the dbName of the db')
   # parser.add_argument('--u', help='the user of the db')
   # parser.add_argument('--pd', help='the password of the db')
    #args = parser.parse_args()

    # 执行
    shell = OsMemoryCheck().check()


