__author__ = 'litu'

#from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil
from com.wangyin.cds.monitor.utils.configUtil import ConfigUtil
from com.wangyin.cds.monitor.utils.cdsUtil import CDSUtil
from com.wangyin.cds.monitor.scheduler.monitorScheduler import MonitorScheduler
class Agent:

    #logger = LoggerUtil.getLogger('Agent')

    def __init__(self):
        ConfigUtil().init_host_ip()
        self.events = CDSUtil.getEvents(CDSUtil)
        self.monitorScheduler = MonitorScheduler(self.events)
    def start(self):
       self.monitorScheduler.start()
    def stop(self):
       self.monitorScheduler.stop()

if __name__ == '__main__':
    Agent().start()


