#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/7 21:24
# @Author : 心蓝
import unittest
import json
from decimal import Decimal

from common.base_test_case import BaseTestCase
from common.fixture import register, login, recharge
from common.test_data_handler import replace_args

from libs.my_ddt import ddt, data


@ddt
class TestWithdraw(BaseTestCase):
    name = '提现接口'
    cases = BaseTestCase.load_cases('withdraw')
    auth_key = 'v2'

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        phone = cls.get_unused_phone_num()
        pwd = '12345678'
        # 1. 注册
        register(phone, pwd)
        # 2. 登录
        res = login(phone, pwd)
        # 登录状态还需要保持，用例间要共享
        # 将登录状态信息保存在类属性中进行用例间共享
        cls.member_id = res['id']
        cls.token = res['token_info']['token']
        # 3. 充值
        recharge(cls.member_id, 500000, cls.token)
        recharge(cls.member_id, 3000, cls.token)

    @data(*cases)
    def test_withdraw(self, case):
        self.logger.info('开始测试：{}'.format(case['title']))
        # 1. 测试数据
        # 1.1 参数替换
        case['request_data'] = replace_args(case['request_data'], member_id=self.member_id)
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])
        # 2. 测试步骤
        if case['sql']:
            # 获取提现之前的余额
            sql = 'select leave_amount from member where id={}'.format(self.member_id)
            before_leave_amount = self.db.get_one(sql)['leave_amount']
            self.logger.info('查询提现前的余额：{}'.format(sql))
        url = self.settings.PROJECT_HOST + self.settings.INTERFACE[case['interface']]
        headers = {'authorization': 'Bearer '+self.token}
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
            # 1. 提现前后的余额

            # 获取提现之后的余额
            sql = 'select leave_amount from member where id={}'.format(self.member_id)
            current_leave_amount = self.db.get_one(sql)['leave_amount']
            self.logger.info('查询提现后的余额：{}'.format(sql))
            try:
                # 提现前余额 - 提现额 = 提现后的余额
                self.assertEqual(before_leave_amount-Decimal(str(request_data['amount'])), current_leave_amount)
                # 接口返回的余额，是否与当前查询的余额一致
                self.assertEqual(current_leave_amount, Decimal(str(res['data']['leave_amount'])))
            except Exception as e:
                self.logger.exception('{}测试数据库校验余额失败'.format(case['title']))
                self.logger.warning('提现前余额：{}'.format(before_leave_amount))
                self.logger.warning('提现金额: {}'.format(request_data['amount']))
                self.logger.warning('提现后余额：{}'.format(current_leave_amount))
                raise e
            # 2. 是否生成了流水记录
            # 2.1 sql
            query_log_sql = 'select id from financelog where pay_member_id={} and \
            amount={} and pay_member_money={}'.format(
                self.member_id,
                request_data['amount'],
                current_leave_amount
            )
            is_create_log = self.db.exist(query_log_sql)
            self.logger.info('查询提现后是否生成了记录: {}'.format(query_log_sql))
            try:
                self.assertTrue(is_create_log)
            except Exception as e:
                self.logger.exception('{}测试生成流水记录校验数据库失败'.format(case['title']))
                raise e


if __name__ == '__main__':
    unittest.main()