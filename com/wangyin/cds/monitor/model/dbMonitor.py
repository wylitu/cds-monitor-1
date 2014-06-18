# -*- coding: utf-8 -*-
__author__ = 'litu'

class DbMonitorConfig:
    def __init__(self, group_id, monitor_item,monitor_item_name, retry_num, check_interval):
        self.group_id = group_id
        self.monitor_item = monitor_item
	self.monitor_item_name = monitor_item_name
        self.retry_num = retry_num
        self.check_interval = check_interval
        self.dbMonitorIndexs = []

    def getGroupId(self):
        return self.group_id
    
    def getMonitorItem(self):
        return self.monitor_item

    def getMonitorItemName(self):
        return self.monitor_item_name

    def getRetryNum(self):
        return self.retry_num

    def getCheckInterval(self):
        return self.check_interval

    def getDbMonitorIndexs(self):
        return self.dbMonitorIndexs

    def add_monitorIndex(self, dbMonitorIndex):
        return self.dbMonitorIndexs.append(dbMonitorIndex)

class MonitorIndexConfig:
    def __init__(self,index_item,index_item_name,index_power,upper,lower):
        self.index_item = index_item
        self.index_item_name = index_item_name
        self.index_power = index_power
        self.upper = upper
        self.lower = lower

    def getIndexItem(self):
        return self.index_item

    def getIndexItemName(self):
        return self.index_item_name

    def getIndexPower(self):
        return self.index_power

    def getUpper(self):
        return self.upper

    def getLower(self):
        return self.lower




