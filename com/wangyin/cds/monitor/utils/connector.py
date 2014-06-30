# -*- coding: utf-8 -*-
import ConfigParser
from mysql import connector
from mysql.connector import Error
from mysql.connector import errorcode
#from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil


class DbConnector:
    #logger = LoggerUtil.getLogger('DbConnector')

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('../config/cds.cfg')

    def new_master_conn(self,cls):
        try:
            h = self.config.get('master','host')
            p = self.config.getint('master','port')
            s = self.config.get('master','db')
            u = self.config.get('master','user')
            k = self.config.get('master','pwd')
            cnx = connector.connect(user=u,password=k,host=h,database=s,port=p)
            return cnx
        except Error as err:
            cls.logger.error(err)
        return None

    def new_slave_conn(self,cls):
        try:
            h = self.config.get('slave','host')
            p = self.config.getint('slave','port')
            s = self.config.get('slave','db')
            u = self.config.get('slave','user')
            k = self.config.get('slave','pwd')
            cnx = connector.connect(user=u,password=k,host=h,database=s,port=p)
            return cnx
        except Error as e:
            cls.logger.error(e.msg,e)
        return None

    def new_group_conn(self,cls):
        try:
            h = self.config.get('slave','host')
            p = self.config.getint('slave','port')
            s = self.config.get('slave','db')
            u = self.config.get('slave','user')
            k = self.config.get('slave','pwd')
            cnx = connector.connect(user=u,password=k,host=h,database=s,port=p)
            return cnx
        except Error as e:
            cls.logger.error(e.msg,e)
        return None
