__author__ = 'wylitu'
class MonitorTaskEvent:
     def __init__(self, monitorIds, dbInfo):
        self.dbInfo = dbInfo
        self.monitorIds = []

     def getDbInfo(self):
         return self.dbInfo
     def getMonitorIds(self):
         return self.monitorIds