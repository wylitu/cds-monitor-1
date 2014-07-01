# coding: utf-8
__author__ = 'wylitu'
import ConfigParser
from ipUtil import  IpUtil
from com.wangyin.cds.monitor.model.monitorTaskEvent import MonitorTaskEvent
class ConfigUtil :

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('../config/agent.cfg')

    def setEvents(self,events):
        if events == None:
            return
        monitorId = ''
        eventId = ''
        for event in events:
             monitorId =  monitorId.__add__(str(event.monitorId)).__add__(',')
             eventId = eventId.__add__(event.eventId).__add__(',')
        self.config.set('events', 'eventid',eventId[:-1])
        self.config.set('events', 'monitorid',monitorId[:-1])
        self.config.write(open('../config/agent.cfg', 'w'))

    def getEventId(self,monitorId=''):
        if monitorId == None:
            return None
        monitorIds =  self.config.get('events', 'monitorId').split(',')
        eventIds =  self.config.get('events', 'eventId').split(',')
        i=0
        for id in monitorIds:
             if id == monitorId:
                 return eventIds[i]
             i = i+1
        return None

    def set_host_ip(self,ip):
        if ip == None:
            return None
        self.config.set('monitorHost', 'host',ip)
        self.config.write(open('../config/agent.cfg', 'w'))
        return None

    def get_host_ip(self):
        ip = self.config.get('monitorHost', 'host')
        if ip == '':
            ip = IpUtil().get_local_ip()
            self.set_host_ip(ip)
        return ip

    def init_host_ip(self):
        ip = IpUtil().get_local_ip()
        self.set_host_ip(ip)

if __name__ == '__main__':
    #print ConfigUtil().get_host_ip()
    events =[]
    events.append(MonitorTaskEvent('22222', 'ddsd','1', None))
    ConfigUtil().setEvents(events)
