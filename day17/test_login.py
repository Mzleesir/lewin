#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/13 22:18
# @Author : 心蓝
import unittest

from ddt import ddt, data

from day17.login import login_check
from day17.test_data_handler import get_data_from_excel

# 获取excel中的测试用例数据
cases = get_data_from_excel('cases.xlsx', sheet_name='login')

@ddt
class TestLogin(unittest.TestCase):

    @data(*cases)
    def test_login(self, case):
        # 1. 测试数据
        # 2. 测试步骤
        res = login_check(username=case['username'], password=case['password'])
        # 3. 断言
        self.assertEqual(case['expect'], res)


