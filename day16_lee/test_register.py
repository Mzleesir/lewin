# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 5:06 下午
# @Author  : Lewin
# @FileName: test_register.py
# @Software: PyCharm
import unittest
from ddt import ddt, data
from day16_lee.register import register


cases = [
    {'title': '注测成功', 'username': 'python34', 'password1': '123456', 'password2': '123456',
     'expect': {"code": 1, "msg": "注册成功"}},
    {'title': '用户名为空', 'username': '', 'password1': '123456', 'password2': '123456',
     'expect': {"code": 0, "msg": "所有参数不能为空"}},
    {'title': '密码为空', 'username': 'python35', 'password1': '', 'password2': '',
     'expect': {"code": 0, "msg": "所有参数不能为空"}},
    {'title': '两次密码不一致', 'username': 'python35', 'password1': '123456', 'password2': '1234567',
     'expect': {"code": 0, "msg": "两次密码不一致"}},
    {'title': '账户已存在', 'username': 'python34', 'password1': '123456', 'password2': '123456',
     'expect': {"code": 0, "msg": "该账户已存在"}},
    {'title': '密码长度小于6位', 'username': 'python35', 'password1': '12345', 'password2': '12345',
     'expect': {"code": 0, "msg": "账号和密码必须在6-18位之间"}},
    {'title': '密码长度大于18位', 'username': 'python35', 'password1': '1234567890123456789',
     'password2': '1234567890123456789', 'expect': {"code": 0, "msg": "账号和密码必须在6-18位之间"}}

]
@ddt
class TestRegister(unittest.TestCase):
    """
    创建一个测试类
    """

    @data(*cases)
    def test_register(self, case):

        # 测试数据 case = {'username': 'python34', 'password1': '123456', 'password2': '123456', 'expect': {"code": 1,
        # "msg": "注册成功"}} 测试步骤
        res = register(username=case['username'], password1=case['password1'], password2=case['password2'])
        # 期望数据
        expect_data=case['expect']
        # 断言
        self.assertEqual(expect_data, res)


if __name__ == '__main__':
    unittest.main()




