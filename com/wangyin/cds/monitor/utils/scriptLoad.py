# coding: utf-8
__author__ = 'wylitu'
import urllib2
import ConfigParser

"load monitor script from cds server"
class ScriptLoad:

   config = ConfigParser.ConfigParser()
   config.read('../config/agent.cfg')

   @staticmethod
   def load(url,cls):
       serverHost = cls.config.get("cdsServer","host")
       port = cls.config.get("cdsServer","port")
       url ='http://'.__add__(serverHost).__add__(":").__add__(port).__add__(url)
       print(url)
       req = urllib2.Request(url)
       f = urllib2.urlopen(req)
       strs= url.split('/')
       scriptName = strs[len(strs)-1]
       print f
       with open("../scripts/"+scriptName, "wb") as code:
            content = f.read()
            content.decode('utf8')
            code.write(content)

if __name__ == '__main__':
    ScriptLoad.load('/script/mysql_dbHang_check.py',ScriptLoad)






