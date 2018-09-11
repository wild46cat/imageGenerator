#!/usr/bin/python
# -*- coding:utf8 -*-
import logging.config

WORK_SPACE = '/Users/wuxueyou/Project/python/imageGenerator'

# 读取日志配置文件内容
logging.config.fileConfig('%s/resources/logging.conf' % WORK_SPACE)

# 创建一个日志器logger
logger = logging.getLogger('app')

if __name__ == '__main__':
    logger.debug("debug")
    logger.info("info")
    logger.warn("warn")
    logger.error("error")
