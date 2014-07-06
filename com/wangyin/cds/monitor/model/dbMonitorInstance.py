# -*- coding: utf-8 -*-
__author__ = 'litu'

class DbMonitorInstance:

    def __init__(self, db_monitor_id,db_info_id, monitor_item, creation_date,error_num, monitor_value,alarm_msg,monitor_type,unit):
        self.db_monitor_id = db_monitor_id
        self.db_info_id = db_info_id
        self.monitor_item = monitor_item
        self.creation_date = creation_date
        self.error_num = error_num
        self.monitor_value = monitor_value
        self.alarm_msg = alarm_msg
        self.monitor_type = monitor_type
        self.unit = unit





