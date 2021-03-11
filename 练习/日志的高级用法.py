# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 11:14 上午
# @Author  : Lewin
# @FileName: 日志的高级用法.py
# @Software: PyCharm
import logging

# 1.创建日志器
logger = logging.getLogger('py34')
logger.setLevel(logging.DEBUG)  # 设置日志等级
# 2.创建日志处理器
file_handler = logging.FileHandler(filename='py34.log', encoding='utf-8')
file_handler.setLevel(logging.WARNING)  # 设置写入文件的等级

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # 设置控制台输出的等级

# 3.创建格式化器
formatter = logging.Formatter(fmt='%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s')
# 4.把格式化器添加到日子处理器
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 5.把日志处理器添加到日志器上
logger.addHandler(file_handler)
logger.addHandler(console_handler)


logger.info("this is a info log")


