# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 8:52 下午
# @Author  : Lewin
# @FileName: main.py
# @Software: PyCharm
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    ts = unittest.TestLoader().discover('..')
    br = BeautifulReport(ts)
    br.report('report.html')