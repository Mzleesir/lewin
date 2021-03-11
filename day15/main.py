# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 9:45 下午
# @Author  : Lewin
# @FileName: main.py
# @Software: PyCharm
import unittest
from BeautifulReport import BeautifulReport

ts = unittest.TestLoader().discover("/Users/lewin/pythonProject/柠檬班/day15")

if __name__ == '__main__':
    br = BeautifulReport(ts)
    br.report('lewin的报告', "report.html")