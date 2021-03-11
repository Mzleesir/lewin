#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/5 20:23
# @Author : 心蓝
import json
import unittest

from libs.my_ddt import ddt, data

from common.base_test_case import BaseTestCase
from common.fixture import register, login, add_loan
from common.test_data_handler import replace_args


@ddt
class AuditTest(BaseTestCase):
    name = '审核项目接口'
    cases = BaseTestCase.load_cases('audit')
    auth_key = 'v2'

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        # 1. 注册普通用户并登陆
        phone = cls.get_unused_phone_num()
        pwd = '12345678'
        register(phone, pwd)
        res = login(phone, pwd)
        # 2. 保存登录状态
        # 将登录状态信息保存在类中进行用例间共享
        # 用户id
        cls.normal_member_id = res['id']
        # token
        cls.normal_token = res['token_info']['token']

        # 2. 注册admin用户并登陆
        phone = cls.get_unused_phone_num()
        pwd = '12345678'

        register(phone, pwd, type_=0)

        res = login(phone, pwd)
        cls.admin_member_id = res['id']
        cls.admin_token = res['token_info']['token']

    def setUp(self) -> None:
        """
        方法级前置
        :return:
        """
        res = add_loan(member_id=self.normal_member_id, token=self.normal_token)
        # 保存在对象中
        self.loan_id = res['data']['id']

    @data(*cases)
    def test_audit(self, case):
        self.logger.info('开始测试：{}'.format(case['title']))
        # 1. 测试数据
        # 替换参数
        case['request_data'] = replace_args(case['request_data'], loan_id=self.loan_id)

        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])

        # 2. 测试步骤
        url = self.settings.PROJECT_HOST + self.settings.INTERFACE['audit']
        headers = {'authorization': 'Bearer ' + self.admin_token}
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
            self.logger.warning('响应回的数据是：{}'.format(res))
            raise e

        # 4. 数据库校验
        if case['sql']:
            # 状态是否发生改变
            sql = case['sql'].replace('#loan_id#', str(self.loan_id))
            is_changed = self.db.exist(sql)
            self.logger.info('查询标状态是否正确：{}'.format(sql))
            try:
                self.assertTrue(is_changed)
            except AssertionError as e:
                self.logger.exception('{}测试数据库校验标审核状态失败'.format(case['title']))
                raise e


if __name__ == '__main__':
    unittest.main()
