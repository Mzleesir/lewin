#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/16 21:36
# @Author : 心蓝
# 日志的组件
# 1. loggers  日志器，产生日志的
# 2. Handler  日志处理器，将日志发送到指定的位置，文件中，控制台
# 3. Filter   日志过滤器  过滤日志  (不常用)
# 4. Formatter  日志格式器  用于控制日志的输出格式


# 日志步骤
# 1. 创建日志器
import logging
logger = logging.getLogger('py34')
logger.setLevel(logging.DEBUG)  # 设置等级
# 2. 创建日志处理器
file_handler = logging.FileHandler(filename='py34.log', encoding='utf-8')
file_handler.setLevel(logging.WARNING)  # 设置写入文件的日志等级

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # 设置控制台输出日志的等级
# 3. 创建格式化器
formatter = logging.Formatter(fmt='%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s')
# 4. 把格式化器添加到日志处理器上
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# 5. 把日志处理器添加到日志器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info('This is a info log')