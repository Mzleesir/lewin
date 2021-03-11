# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 9:26 下午
# @Author  : Lewin
# @FileName: test_register.py
# @Software: PyCharm
import unittest
import json

from 练习.my_ddt import ddt, data
from 练习.register import register
from 练习.test_data_handler import get_data_from_excel

cases = get_data_from_excel('cases.xlsx', sheet_name='register')


@ddt
class TestRegister(unittest.TestCase):
    @data(*cases)
    def test_register(self, case):
        # 1.测试数据
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])

        # 2.测试步骤
        res = register(**request_data)
        self.assertEqual(expect_data, res)
