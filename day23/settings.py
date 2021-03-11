#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/27 20:21
# @Author : 心蓝
# 配置文件
import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 测试数据配置
TEST_DATA_FILE = os.path.join(BASE_DIR, 'testdata', 'testcases.xlsx')

# 测试用例路径
TEST_CASE_DIR = os.path.join(BASE_DIR, 'testcases')
# 配置报告
TEST_REPORT_CONFIG = {
    'file': 'py34测试报告.html',
    'report_dir': os.path.join(BASE_DIR, 'reports'),
    'title': 'py34期测试报告',
    'description': None,
    'tester': '心蓝',
    'type_': 'htr'  # htr htmltestrunner  bf beautifulreport
}
# 日志配置
LOG_CONFIG = {
    'name': 'py34',
    'file': os.path.join(BASE_DIR, 'log', 'py34.log'),
    'fmt': '%(levelname)s %(asctime)s [%(filename)s-->line:%(lineno)d]:%(message)s',
    'debug': False
}
# print(LOG_CONFIG)
# 路径拼接
# print(BASE_DIR + '\\' + 'log' + '\\' + 'py34.log')
# print(os.path.join(BASE_DIR, 'log', 'py34.log'))

















# 路径解决
# print(__file__)
#
# print(os.path.abspath(__file__))
#
# print(os.path.dirname('D:/project/py34/day23/settings.py'))
# # 当前脚本所在的绝对路径
# print(os.path.dirname(os.path.abspath(__file__)))

