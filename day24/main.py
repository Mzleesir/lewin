#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 21:55
# @Author : 心蓝
import unittest

from BeautifulReport import BeautifulReport

import settings
from common.report_handler import report


if __name__ == '__main__':
    ts = unittest.TestLoader().discover(settings.TEST_CASE_DIR)
    report(ts, **settings.TEST_REPORT_CONFIG)
    # bs = BeautifulReport(ts)
    # bs.report('reports/report.html')
