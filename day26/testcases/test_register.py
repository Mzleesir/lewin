#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 21:19
# @Author : 心蓝
import json
import unittest

from libs.my_ddt import ddt, data

from common.base_test_case import BaseTestCase


@ddt
class TestRegister(BaseTestCase):   #  classname('testmethod')

    name = '注册接口'

    cases = BaseTestCase.load_cases('register')

    @data(*cases)
    def test_register(self, case):
        # 1. 测试数据
        # request_data, expect_data
        # 判断一下是否需要生成手机号码
        if '#phone#' in case['request_data']:

            # 需要进行手机号码替换
            phone = self.get_unused_phone_num("select id from member where mobile_phone='{}'")
            self.logger.info('生成手机号码:{}'.format(phone))
            case['request_data'] = case['request_data'].replace('#phone#', phone)

            # 还需要替换sql中phone
            if case['sql']:
                case['sql'] = case['sql'].replace('#phone#', phone)

        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])
        # 2. 测试步骤

        url = self.settings.PROJECT_HOST + self.settings.INTERFACE[case['interface']]
        res = self.send_request(url=url, method=case['method'], json=request_data).json()
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
            try:
                self.logger.info('执行的sql是：{}'.format(case['sql']))
                self.assertTrue(self.db.exist(case['sql']))
            # self.assertEqual(True, db.exist())
            except Exception as e:
                self.logger.exception('{}::数据库校验失败'.format(case['title']))

                raise e


if __name__ == '__main__':
    unittest.main()