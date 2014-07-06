# -*- coding: utf-8 -*-
__author__ = 'litu'

class DbConfig:

    def __init__(self,db_info_id,group_id,ip,user_name,passwd,port,db_type):
        self.group_id = group_id
        self.ip = ip
        self.port = port
        self.user_name = user_name
        self.passwd = passwd
        self.db_info_id = db_info_id
        self.db_type = db_type
        self.db_units = {}

    def add_db_unit(self,dbUnit):
        self.db_units.append(dbUnit)

class DbUnit:

    def __init__(self,ip,port,db_name,user_name, passwd,masterOrSlave,db_type):
        self.ip = ip
        self.port = port
        self.db_name = db_name
        self.masterOrSlave = masterOrSlave
        self.db_type = db_type
        self.user_name = user_name
        self.passwd = passwd


