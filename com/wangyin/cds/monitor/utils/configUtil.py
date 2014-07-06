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
        if events == None or len(events) == 0:
            return
        eventId_Type = ''
        for event in events:
             eventId_Type = eventId_Type.__add__(str(event.eventId)).__add__('_').__add__(event.eventType).__add__(',')
        self.config.set('events', 'eventid_eventtype',eventId_Type[:-1])
        self.config.write(open('../config/agent.cfg', 'w'))

    def is_config_has_event(self,event):
        if event == None:
            return False
        eventid_types =  self.config.get('events', 'eventid_eventtype').split(',')
        if len(eventid_types) == 0 :
            return False
        for eventid_type in eventid_types:
             eventid_type_new = str(event.eventId).__add__('_').__add__(event.eventType)
             if  eventid_type_new == eventid_type:
                 return True
        return False

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
    events.append(MonitorTaskEvent('2223', 'ddsd','2', None))
    ConfigUtil().setEvents(events)
