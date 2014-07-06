# coding: utf-8
__author__ = 'wylitu'
import urllib2,urllib,json
from urllib import quote
from apscheduler.scheduler import Scheduler
import ConfigParser

"load monitor script from cds server"
class ScriptLoad:

   config = ConfigParser.ConfigParser()
   config.read('../config/agent.cfg')

   def load(self):
       sched = Scheduler()
       sched.daemonic = False
       # Schedules job_function to be run on the third Friday
   # of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
       sched.add_cron_job(self.job_function, second='*/3')
       sched.start()
   def job_function(self):
       print "Hello World"



if __name__ == '__main__':
    ScriptLoad().load()