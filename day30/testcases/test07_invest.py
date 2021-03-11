#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/7 14:35
# @Author : 心蓝
import unittest
import json
from decimal import Decimal

from common.base_test_case import BaseTestCase
from common.test_data_handler import extract_data, replace_args_by_re
from common.encrypt_handler import generator_sign
from libs.my_ddt import ddt, data


@ddt
class TestInvest(BaseTestCase):
    name = '投资接口'
    auth_key = 'v3'

    cases = BaseTestCase.load_cases('invest')

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        # 生成3不同角色的手机号码
        cls.phone = cls.get_unused_phone_num()
        cls.invest1_phone = cls.get_unused_phone_num()
        cls.invest2_phone = cls.get_unused_phone_num()
        cls.admin_phone = cls.get_unused_phone_num()

    @data(*cases)
    def test_invest(self, case):
        self.logger.info('开始测试：{}'.format(case['title']))
        # 1. 处理测试数据
        # 1.1 替换json字符串中的需要被替换的参数
        case['request_data'] = replace_args_by_re(case['request_data'], self.__class__)
        # 1.2 反序列化json字符串
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])
        # 2. 测试步骤
        if case['sql']:
            # 获取投资前的余额
            sql = 'select leave_amount from member where id={}'.format(request_data['member_id'])
            before_leave_amount = self.db.get_one(sql)['leave_amount']
            self.logger.info('查询投资前投资者余额：{}'.format(sql))

        # 2.1 发送请求数据准备
        url = self.settings.PROJECT_HOST + self.settings.INTERFACE[case['interface']]
        if case['headers']:
            headers = {'authorization': 'Bearer ' + getattr(self, case['headers'])}  # self.token self.__class__.token
            if self.auth_key == 'v3':
                sign, timestamp = generator_sign(getattr(self, case['headers']))
                request_data['sign'] = sign
                request_data['timestamp'] = timestamp
        else:
            headers = {}
        # 2.2 发送请求
        response = self.send_request(url, case['method'], json=request_data, headers=headers)
        res_text = response.text
        res = response.json()
        # 3. 响应结果校验
        # 3.1 断言
        res_data = {'code': res['code'], 'msg': res['msg']}
        try:
            self.assertEqual(expect_data, res_data)
        except Exception as e:
            self.logger.exception('{}::测试失败'.format(case['title']))
            self.logger.warning('请求数据是: {}'.format(request_data))
            self.logger.warning('期望结果是：{}'.format(expect_data))
            self.logger.warning('实际结果是：{}'.format(res_data))
            self.logger.warning('响应回的数据是：{}'.format(res))
            raise e
        # 4. 提取响应数据
        if case['extract']:
            maps = json.loads(case['extract'])
            extract_data(maps, self.__class__, res_text)

        # 5. 数据库校验
        if case['sql']:
            # 投资后去查询当前余额
            sql = 'select leave_amount from member where id={}'.format(request_data['member_id'])
            current_leave_amount = self.db.get_one(sql)['leave_amount']
            self.logger.info('查询投资后余额：{}'.format(sql))

            # 1. 用户余额的变化
            try:
                self.assertEqual(before_leave_amount-Decimal(str(request_data['amount'])), current_leave_amount)
            except Exception as e:
                self.logger.error('校验用户投资余额失败: 投资前余额:{},投资额：{},投资后余额:{}'.\
                                  format(before_leave_amount, request_data['amount'], current_leave_amount))
                raise e
            # 2. 投资记录
            sql = 'select id from invest where member_id={member_id} and loan_id={loan_id} and amount={amount} \
                        and is_valid=1'.format(**request_data)
            self.logger.info('查询投资记录是否生成：{}'.format(sql))
            is_create_invest_log = self.db.exist(sql)
            try:
                self.assertTrue(is_create_invest_log)
            except Exception as e:
                self.logger.error('生成投资记录失败')
                raise e

            # 3. 流水记录
            sql = 'select id from financelog where pay_member_id={member_id} and amount={amount} and \
            pay_member_money={current_leave_amount} and status=1'\
                .format(**request_data, current_leave_amount=current_leave_amount)
            is_create_finance_log = self.db.exist(sql)
            self.logger.info('查询流水记录是否生成:{}'.format(sql))
            try:
                self.assertTrue(is_create_finance_log)
            except Exception as e:
                self.logger.error('生成流水记录失败')
                raise e
            # 4. 还款记录
            loan_amount = self.db.get_one('select amount from loan where id={}'.format(
                request_data['loan_id']))['amount']
            invest_total_amount = self.db.get_one('select sum(amount) as total from invest where loan_id={} \
            and is_valid=1'.format(request_data['loan_id']))['total']
            if loan_amount == invest_total_amount:
                self.logger.info('满标了')
                invest_logs = self.db.get_all('select id as invest_id, amount from invest where \
                loan_id={} and is_valid=1'.format(request_data['loan_id']))
                for item in invest_logs:
                    check_sql = 'select id from repayment where invest_id={invest_id} \
                    and unfinished_principal={amount}'.format(**item)
                    if not self.db.exist(check_sql):
                        self.logger.error('生成汇款记录失败，sql:{}'.format(check_sql))
                        raise AssertionError('生成汇款记录失败！')


if __name__ == '__main__':
    unittest.main()