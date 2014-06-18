# coding: utf-8
import logging
class LoggerUtil:

    logging.config.fileConfig('../config/logger.conf')

    @staticmethod
    def getLogger(name):
        return logging.getLogger(name)


