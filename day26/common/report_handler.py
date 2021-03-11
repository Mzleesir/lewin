#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/27 21:08
# @Author : 心蓝
# 生成报告
import os
from datetime import datetime

from BeautifulReport import BeautifulReport

from libs.HTMLTestRunnerNew import HTMLTestRunner


def report(ts, file='report.html', report_dir='.', title='测试报告', description=None, tester='那谁谁', type_='htr'):
    """
    生成不同的测试报告
    :param ts: 测试套件
    :param file: 测试报告文件名
    :param report_dir: 测试报告路径
    :param title: 测试标题
    :param description: 测试描述
    :param tester: 测试者
    :param type_: 报告类型
    :return:
    """
    # 在报告文件名上加上时间
    # file = '{}-{}'.format(datetime.now().strftime('%Y-%m-%d %H时%M分%S秒'), file)
    file = '{}-{}'.format(datetime.now().strftime('%Y-%m-%d %H{}%M{}%S{}').format('时','分','秒'), file)
    # 检测一下目录是否存在，不存在要创建
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    # 拼接报告文件名
    file_path = os.path.join(report_dir, file)
    # 生成报告
    if type_.lower() == 'htr':
        with open(file_path, 'wb') as f:
            runner = HTMLTestRunner(f, title=title, description=description, tester=tester)
            runner.run(ts)
    else:
        br = BeautifulReport(ts)
        br.report(filename=file, description=description, report_dir=report_dir)


# nw = datetime.now()
# print(nw ,type(nw))
# print(nw.strftime('%Y-%m-%d %H时%M分%S秒'))
# import time
# # time.strftime()
# print('{}-{}'.format(datetime.now().strftime('%Y-%m-%d %H时%M分%S秒'), 'report.html'))