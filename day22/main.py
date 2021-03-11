#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 21:55
# @Author : 心蓝
import unittest
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    ts = unittest.TestLoader().discover('.')
    bs = BeautifulReport(ts)
    bs.report('report.html')
