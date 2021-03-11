#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/13 20:51
# @Author : 心蓝
import unittest

from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    ts = unittest.TestLoader().discover('.')
    print(ts)
    br = BeautifulReport(ts)
    br.report('report.html')
