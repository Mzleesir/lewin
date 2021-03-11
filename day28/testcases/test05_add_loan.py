#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/5 19:35
# @Author : 心蓝
import json
import unittest

from libs.my_ddt import ddt, data

from common.base_test_case import BaseTestCase
from common.fixture import register, login
from common.test_data_handler import replace_args


@ddt
class AddLoanTest(BaseTestCase):
    name = '创建项目接口'
    cases = BaseTestCase.load_cases('add')
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
    def test_add_loan(self, case):
        self.logger.info('开始测试：{}'.format(case['title']))
        # 1. 测试数据
        # 替换参数
        case['request_data'] = replace_args(case['request_data'], member_id=self.member_id)

        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])

        # 2. 测试步骤
        url = self.settings.PROJECT_HOST + self.settings.INTERFACE['add']
        headers = {'authorization': 'Bearer ' + self.token}

        self.logger.warning('发送请求的token:{}'.format(self.token))
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
            # loan数据库中是否添加一条记录
            sql = 'select id from loan where id={} and member_id={member_id} and title="{title}" \
            and amount={amount} and loan_rate={loan_rate} and loan_term={loan_term} and \
            loan_date_type={loan_date_type} and bidding_days={bidding_days}'.format(res['data']['id'], **request_data)
            is_add_a_record = self.db.exist(sql)
            self.logger.info('查询loan表中是否增加一个标：{}'.format(sql))
            try:
                self.assertTrue(is_add_a_record)
            except AssertionError as e:
                self.logger.exception('{}测试数据库校验新增记录失败'.format(case['title']))
                raise e


if __name__ == '__main__':
    unittest.main()
