# coding: utf-8
__author__ = 'wylitu'
import urllib2,urllib
from urllib import quote
import ConfigParser,os

"load monitor script from cds server"
class ScriptLoad:

   def __init__(self):
       self.config = ConfigParser.ConfigParser()
       self.config.read('../config/agent.cfg')

   def load(self,url):
       serverHost = self.config.get("cdsServer","host")
       port = self.config.get("cdsServer","port")
       scriptName = url
       url ='http://'+serverHost+":"+str(port)+"/script/"+url
       req = urllib2.Request(url)
       f = urllib2.urlopen(req)
       scripFilePath = "../scripts/"+scriptName
       if os.path.exists(scripFilePath) == False:
           os.mkdir("../scripts/"+scripFilePath.split('/')[2])

       with open(scripFilePath, "wb") as code:
            content = f.read()
            #content.decode('utf8')
            code.write(content)

#if __name__ == '__main__':
    #ScriptLoad().load('test/mysql_dbHang_check.py')






