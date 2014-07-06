# -*- coding: utf-8 -*-
__author__ = 'litu'

class DbMonitorConfig:
    def __init__(self,id,group_id, monitor_item, check_times,retry_num, check_interval,scriptType,scriptPath,monitor_type,unit):
        self.id = id
        self.group_id = group_id
        self.monitor_item = monitor_item
        self.check_times = check_times
        self.retry_num = retry_num
        self.check_interval = check_interval
        self.scriptPath = scriptPath
        self.scriptType = scriptType
        self.monitor_type = monitor_type
        self.unit = unit




