#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/16 21:20
# @Author : 心蓝
import logging
# 记录日志的等级有过滤功能
# 默认情况下logging的日志等级是warning
# 配置
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志等级
    format='%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s',
    filename='log.log'
)
logging.debug('This is a debug log')        # 调试
logging.info('This is a info log')          # 信息
logging.warning('This is a warning log')    # 警告
logging.error('This is a error log')        # 错误
logging.critical('This is a critical log')  # 致命

