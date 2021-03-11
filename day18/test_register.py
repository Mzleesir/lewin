#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/16 20:18
# @Author : 心蓝
import unittest
import json

from day18.my_ddt import ddt, data

from day18.register import register
from day18.test_data_handler import get_data_from_excel
from day18.log_handler import logger

cases = get_data_from_excel('cases.xlsx', sheet_name='register')


@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('============开始测试注册功能================')

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('============测试注册功能结束================')

    @data(*cases)
    def test_register(self, case):
        """
        测试注册
        :param case:
        :return:
        """
        # 1. 测试数据
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])
        # 2. 测试步骤
        res = register(**request_data)
        # 3. 断言
        try:
            self.assertEqual(expect_data, res)
        except Exception as e:
            logger.warning('{}:测试失败'.format(case['title']))
            logger.warning('测试数据是：{}'.format(request_data))
            logger.warning('测试结果是：{}'.format(res))
            logger.warning('期望结果是：{}'.format(expect_data))
            # 一定要抛出这个异常
            raise e
