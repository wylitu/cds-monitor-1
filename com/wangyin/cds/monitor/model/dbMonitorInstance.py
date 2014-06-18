# -*- coding: utf-8 -*-
__author__ = 'litu'

class DbMonitorInstance:
    group_id =0
    def __init__(self, group_id, monitor_item, monitor_item_name,error_num, alarm_msg):
        self.group_id = group_id
        self.monitor_item = monitor_item
	self.monitor_item_name = monitor_item_name
        self.error_num = error_num
        self.alarm_msg = alarm_msg
        self.dbMonitorIndexInstances = []

    def getGroupId(self):
        return self.group_id
    
    def getMonitorItem(self):
        return self.monitor_item

    def getMonitorItemName(self):
        return self.monitor_item_name

    def getErrorNum(self):
        return self.error_num

    def getAlarmMsg(self):
        return self.alarm_msg

    def add_monitorIndexInstance(self, dbMonitorIndexInstance):
        return self.dbMonitorIndexInstances.append(dbMonitorIndexInstance)

    def getMonitorIndexInstances(self):
        return self.dbMonitorIndexInstances

class MonitorIndexInstance:
    def __init__(self,index_item,index_item_name,value):
        self.index_item_name = index_item_name
        self.index_item = index_item
        self.value = value

    def getIndexItem(self):
        return self.index_item

    def getIndexItemName(self):
        return self.index_item_name

    def getValue(self):
        return self.value




