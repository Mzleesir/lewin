#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 21:19
# @Author : 心蓝
import json
import unittest

from libs.my_ddt import ddt, data

import settings
from common.test_data_handler import get_data_from_excel
from common.request_handler import send_request
from common.log_handler import logger

cases = get_data_from_excel(settings.TEST_DATA_FILE, sheet_name='register')

@ddt
class TestRegister(unittest.TestCase):
    logger = logger
    # 鉴权方式
    auth_key = 'v1'

    @classmethod
    def setUpClass(cls) -> None:
        # 类前置
        cls.logger.info('==========注册接口测试开始============')
        # print('==========注册接口测试开始============')

    @classmethod
    def tearDownClass(cls) -> None:
        # 类后置
        cls.logger.info('==========注册接口测试结束============')
        # print('==========注册接口测试结束============')

    @data(*cases)
    def test_register(self, case):
        # 1. 测试数据
        # request_data, expect_data
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])
        # 2. 测试步骤
        # headers = {
        #     'X-Lemonban-Media-Type': 'lemonban.v1'
        # }
        headers = settings.CUSTOM_HEADERS[self.auth_key]
        url = settings.PROJECT_HOST + settings.INTERFACE[case['interface']]
        res = send_request(url=url, method=case['method'], json=request_data, headers=headers).json()
        # 3. 断言
        res_data = {'code': res['code'], 'msg': res['msg']}
        # self.assertEqual(expect_data['code'], res['code'])
        # self.assertEqual(expect_data['msg'], res['msg'])
        try:
            self.assertEqual(expect_data, res_data)
        except Exception as e:
            self.logger.exception('{}::测试失败'.format(case['title']))
            self.logger.warning('请求数据是: {}'.format(request_data))
            self.logger.warning('期望结果是：{}'.format(expect_data))
            self.logger.warning('实际结果是：{}'.format(res_data))
            raise e
        # 4. 看下是否要校验数据库？
        if case['sql']:
            # 校验数据库
            # 用代码执行sql
            pass



if __name__ == '__main__':
    unittest.main()