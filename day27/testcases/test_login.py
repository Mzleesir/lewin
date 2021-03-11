#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/4 21:09
# @Author : 心蓝
import json
import unittest

from libs.my_ddt import ddt, data

from common.base_test_case import BaseTestCase


@ddt
class TestLogin(BaseTestCase):
    name = '登录接口'

    # cases = BaseTestCase.load_cases('login')
    #
    # @data(*cases)
    # def test_login(self, case):
    #     # 1.测试数据
    #     # 2.测试步骤
    #     # 3.断言
    #     pass