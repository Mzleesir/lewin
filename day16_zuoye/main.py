# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 3:37 下午
# @Author  : Lewin
# @FileName: main.py
# @Software: PyCharm

import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    # 收集用例
    ts = unittest.TestLoader().discover('.')
    # 运行用例并输出报告
    br = BeautifulReport(ts)
    br.report('report.html')