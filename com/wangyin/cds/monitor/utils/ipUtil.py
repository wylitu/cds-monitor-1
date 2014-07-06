# coding: utf-8
__author__ = 'wylitu'
#import fcntl
import socket,platform,struct

class IpUtil:

    def get_local_ip(self):
         sys = platform.system()
         if(sys =="Windows"):
              myname = socket.getfqdn(socket.gethostname())
              return socket.gethostbyname(myname)
         #elif(sys == "Linux"):
          #    ifname ='eth0'
         #     skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          #    pktString = fcntl.ioctl(skt.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
          #    ipString  = socket.inet_ntoa(pktString[20:24])
          #    return ipString
         return None
if __name__ == '__main__':
    print IpUtil().get_local_ip()
