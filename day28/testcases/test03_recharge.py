#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/5 14:17
# @Author : 心蓝
import json
import unittest
from decimal import Decimal

from libs.my_ddt import ddt, data

from common.base_test_case import BaseTestCase
from common.fixture import register, login
from common.test_data_handler import replace_args


@ddt
class RechargeTest(BaseTestCase):
    name = '充值接口'
    cases = BaseTestCase.load_cases('recharge')
    auth_key = 'v2'

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        # 1. 注册
        phone = cls.get_unused_phone_num()
        pwd = '12345678'
        register(phone, pwd)

        # 2. 登录
        res = login(phone, pwd)

        # 3. 保存登录状态
        # 将登录状态信息保存在类中进行用例间共享
        # 用户id
        cls.member_id = res['id']
        # token
        cls.token = res['token_info']['token']

    @data(*cases)
    def test_recharge(self, case):
        self.logger.info('开始测试：{}'.format(case['title']))
        # 1. 测试数据
        # 替换参数
        case['request_data'] = replace_args(case['request_data'], member_id=self.member_id)
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])

        # 2. 测试步骤
        if case['sql']:
            # 获取充值前的余额
            before_leave_amount = self.db.get_one(
                'select leave_amount from member where id={}'.format(self.member_id))['leave_amount']
            self.logger.info('查询充值前余额：{}'.format(case['sql']))
        url = self.settings.PROJECT_HOST + self.settings.INTERFACE['recharge']
        headers = {'authorization': 'Bearer ' + self.token}
        res = self.send_request(url=url, method=case['method'], json=request_data, headers=headers).json()

        # 3. 断言
        res_data = {'code': res['code'], 'msg': res['msg']}

        try:
            self.assertEqual(expect_data, res_data)
        except Exception as e:
            self.logger.exception('{}::测试失败'.format(case['title']))
            self.logger.warning('请求数据是: {}'.format(request_data))
            self.logger.warning('期望结果是：{}'.format(expect_data))
            self.logger.warning('实际结果是：{}'.format(res_data))
            raise e

        # 4. 数据库校验
        if case['sql']:
            # 充值后去查询当前余额

            current_leave_amount = self.db.get_one(
                'select leave_amount from member where id={}'.format(self.member_id))['leave_amount']
            self.logger.info('查询充值后余额：{}'.format(case['sql']))
            try:
                # 判断接口返回的余额是否与数据库中的一致
                # 注意转变数据类型为Decimal
                self.assertEqual(Decimal(str(res['data']['leave_amount'])), current_leave_amount)
                # 充值后的余额是否等于充值前余额+充值额
                self.assertEqual(before_leave_amount+Decimal(str(request_data['amount'])), current_leave_amount)
            except AssertionError as e:
                self.logger.exception('{}测试数据库校验金额失败'.format(case['title']))
                self.logger.warning('充值前余额：{}'.format(before_leave_amount))
                self.logger.warning('充值金额: {}'.format(request_data['amount']))
                self.logger.warning('充值后余额：{}'.format(current_leave_amount))
                raise e
                # 查询当前用户的进账交易记录

            query_log_sql = 'select id from financelog where income_member_id={} and amount={} and income_member_money={}'.format(
                self.member_id, request_data['amount'], current_leave_amount)

            is_create_log = self.db.exist(query_log_sql)
            self.logger.info('查询充值后是否生成记录: {}'.format(query_log_sql))
            try:
                self.assertTrue(is_create_log)
            except AssertionError as e:
                self.logger.exception('{}测试生成流水记录数据库校验失败'.format(case['title']))


if __name__ == '__main__':
    unittest.main()
