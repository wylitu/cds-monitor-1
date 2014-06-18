# -*- coding: utf-8 -*-
__author__ = 'litu'

class DbInfo:

    def __init__(self,group_id,ip,port,db_name,masterOrSlave,db_type,db_status):
        self.group_id = group_id
        self.ip = ip
        self.port = port
        self.db_name = db_name
        self.masterOrSlave = masterOrSlave
        self.db_type = db_type
        self.db_status = db_status
        
    def getGroupId(self):
        return self.group_id

    def getIp(self):
        return self.ip

    def getPort(self):
        return self.port

    def getDbName(self):
        return self.db_name

    def getMasterOrSlave(self):
        return self.masterOrSlave

    def getDbType(self):
        return self.db_type

    def getDbStatus(self):
        return self.status
    



