# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 9:51 下午
# @Author  : Lewin
# @FileName: test_register.py
# @Software: PyCharm
import unittest
from day18_lee.my_ddt import ddt, data
import json
from day18_lee.test_data_handler import get_data_from_excel
from day18_lee.register import register


cases = get_data_from_excel('cases.xlsx', sheet_name='register')

@ddt
class TestRegister(unittest.TestCase):
    @data(*cases)
    def test_register(self, case):
        # 1.测试数据
        # res = register(username=case['request_data[username]'], password1=case['request_data[password1]'], password2=case['request_data[password2]'])
        # 2.测试步骤
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])
        res = register(**request_data)


        # 3.断言
        self.assertEqual(expect_data, res)



if __name__ == '__main__':
    unittest.main()



