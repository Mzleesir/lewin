#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 21:19
# @Author : 心蓝
import json
import unittest

from day22.my_ddt import ddt, data

from day22.test_data_handler import get_data_from_excel
from day22.request_handler import send_request

cases = get_data_from_excel('testcases.xlsx')


@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 类前置
        print('==========注册接口测试开始============')

    @classmethod
    def tearDownClass(cls) -> None:
        # 类后置
        print('==========注册接口测试结束============')

    @data(*cases)
    def test_register(self, case):
        # 1. 测试数据
        # request_data, expect_data
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])
        # 2. 测试步骤
        headers = {
            'X-Lemonban-Media-Type': 'lemonban.v1'
        }
        res = send_request(url=case['url'], method=case['method'], json=request_data, headers=headers).json()
        # 3. 断言
        res_data = {'code': res['code'], 'msg': res['msg']}
        # self.assertEqual(expect_data['code'], res['code'])
        # self.assertEqual(expect_data['msg'], res['msg'])
        self.assertEqual(expect_data, res_data)


if __name__ == '__main__':
    unittest.main()
