__author__ = 'wylitu'
class MonitorTaskEvent:
     def __init__(self, eventId, eventType, monitorId, dbConfig):
        self.eventId = eventId
        self.eventType = eventType
        self.dbConfig = dbConfig
        self.monitorId = monitorId
