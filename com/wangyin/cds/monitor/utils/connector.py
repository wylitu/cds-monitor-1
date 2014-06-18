# -*- coding: utf-8 -*-
import ConfigParser
from mysql import connector
from mysql.connector import Error
from mysql.connector import errorcode
from com.wangyin.cds.monitor.utils.loggerUtil import LoggerUtil


class ClusterConnector:
    logger = LoggerUtil.getLogger('ClusterConnector')

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('../config/cds.cfg')

    def new_master_conn(self):
        try:
            h = self.config.get('master','host')
            p = self.config.getint('backingstore','port')
            s = self.config.get('backingstore','db')
            u = self.config.get('backingstore','user')
            k = self.config.get('backingstore','pwd')
            cnx = connector.connect(user=u,password=k,host=h,database=s,port=p)
            return cnx
        except Error as err:
            print(err)
        return None

    def new_slave_conn(self,host,port,db):
        try:
            user_name = self.config.get('group','user')
            password = self.config.get('group','pwd')
            cnx = connector.connect(user=user_name,password=password, host=host,port=port,database=db)
            return cnx
        except Error as e:
            ClusterConnector.logger.error()
        return None
