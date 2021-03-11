# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 8:45 下午
# @Author  : Lewin
# @FileName: test_login.py
# @Software: PyCharm
import unittest
from ddt import ddt, data
from 练习.login import login_check
from 练习.test_data_handler import test_data_from_excel

cases = test_data_from_excel("cases.xlsx", sheet_name='login')

@ddt
class TestLogin(unittest.TestCase):
    @data(*cases)
    def test_login(self, case):
        # 1.测试数据
        # 2.测试步骤
        res = login_check(username=case['username'], password=case['password'])
        # 3.断言
        self.assertEqual(case['except'], res)



