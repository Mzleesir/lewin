# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 9:59 下午
# @Author  : Lewin
# @FileName: test_register.py
# @Software: PyCharm
import json
import unittest
from lianxi2.my_ddt import ddt, data
from lianxi2.test_data_handler import get_data_from_excel
from lianxi2.requests_handler import send_requests

cases = get_data_from_excel('testcases.xlsx', sheet_name='register')

@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('======注册测试开始======')

    def tearDownClass(cls) -> None:
        print('======注册测试结束======')

    @data(*cases)
    def test_register(self, case):
        # 1.测试数据
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])

        # 2.测试步骤
        headers = {
            'X-Lemonban-Media-Type': 'lemonban.v1'
        }
        res = send_requests(url=case['url'], json = request_data, method=case['method'], headers=headers).json()
        # 3.断言
        res_data = {'code': res['code'], 'msg': res['msg']}
        self.assertEqual(expect_data, res_data)


if __name__ == '__main__':
    unittest.main()


