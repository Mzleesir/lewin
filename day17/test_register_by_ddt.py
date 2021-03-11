#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/13 13:49
# @Author : 心蓝
import unittest

from ddt import ddt, data

from day17.register import register

"""
   注册成功               返回结果：{"code": 1, "msg": "注册成功"}
   有参数为空，            返回结果 {"code": 0, "msg": "所有参数不能为空"}   
   两次密码不一致          返回结果：{"code": 0, "msg": "两次密码不一致"}
   账户已存在             返回结果：{"code": 0, "msg": "该账户已存在"}
   密码不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}              
   账号不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
测试用例

{'title': '注测成功','username': 'python34', 'password1': '123456', 'password2': '123456', 'expect': {"code": 1, "msg": "注册成功"}}
{'title': '用户名为空','username': '', 'password1': '123456', 'password2': '123456', 'expect': {"code": 0, "msg": "所有参数不能为空"}}
{'title': '密码为空','username': 'python35', 'password1': '', 'password2': '', 'expect': {"code": 0, "msg": "所有参数不能为空"}}
{'title': '两次密码不一致','username': 'python35', 'password1': '123456', 'password2': '1234567', 'expect': {"code": 0, "msg": "两次密码不一致"}}
{'title': '账户已存在','username': 'python34', 'password1': '123456', 'password2': '123456', 'expect': {"code": 0, "msg": "该账户已存在"}}
{'title': '密码长度小于6位','username': 'python35', 'password1': '12345', 'password2': '12345', 'expect': {"code": 0, "msg": "账号和密码必须在6-18位之间"}}
{'title': '密码长度大于18位','username': 'python35', 'password1': '1234567890123456789', 'password2': '1234567890123456789', 'expect': {"code": 0, "msg": "账号和密码必须在6-18位之间"}}
"""

a = {'title': '密码长度大于18位', 'username': 'python35', 'password1': '1234567890123456789',
     'password2': '1234567890123456789', 'expect': {"code": 0, "msg": "账号和密码必须在6-18位之间"}}

b = {'title': '密码长度小于6位', 'username': 'python35', 'password1': '12345', 'password2': '12345',
     'expect': {"code": 0, "msg": "账号和密码必须在6-18位之间"}}

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
class TestRegisterByDDT(unittest.TestCase):

    @data(*cases)
    def test_register(self, case):
        # 1. 测试数据 case
        # 2. 测试步骤
        res = register(
            username=case['username'],
            password1=case['password1'],
            password2=case['password2']
        )
        # 3.断言
        self.assertEqual(case['expect'], res)
