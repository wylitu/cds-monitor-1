__author__ = 'litu'

from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil
from com.wangyin.cds.monitor.utils.configUtil import ConfigUtil
from com.wangyin.cds.monitor.Scheduler.monitorScheduler import MonitorScheduler
class Agent:

    logger = LoggerUtil.getLogger('Agent')

    def __init__(self):
        self.dbConfig = ConfigUtil.getDbConfig()
        self.dbMonitorConfig = ConfigUtil.getDbMonitorConfig()
        self.monitorScheduler = MonitorScheduler(self.dbConfig,self.dbMonitorConfig)

    def start(self):
       self.monitorScheduler.start()
    def stop(self):
       self.monitorScheduler.stop()

    if __name__ == '__main__':
        start()


