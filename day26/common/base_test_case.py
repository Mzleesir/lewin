#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/4 21:14
# @Author : 心蓝
import unittest

import settings
from common.log_handler import logger
from common.db_handler import db
from common.request_handler import send_request
from common.test_data_handler import get_data_from_excel, generate_phone_num


class BaseTestCase(unittest.TestCase):
    name = None   # 功能名称
    logger = logger  # 日志器
    db = db  # 数据库处理对象
    auth_key = 'v1'  # 鉴权请求头
    settings = settings  # 配置模块

    @classmethod
    def setUpClass(cls) -> None:
        # 类前置
        cls.logger.info('=========={}测试开始============'.format(cls.name))
        # print('==========注册接口测试开始============')

    @classmethod
    def tearDownClass(cls) -> None:
        # 类后置
        cls.logger.info('=========={}测试结束============'.format(cls.name))
        # print('==========注册接口测试结束============')

    @classmethod
    def load_cases(cls, sheet_name):
        """
        提取excel文件中的用例数据
        :param sheet_name: 表名
        :return:
        """
        return get_data_from_excel(cls.settings.TEST_DATA_FILE, sheet_name)

    def send_request(self, url, method='GET', **kwargs):
        # 自动处理权限请求头
        kwargs.setdefault('headers', {})
        kwargs['headers'].update(self.settings.CUSTOM_HEADERS[self.auth_key])

        if self.auth_key == 'v2':
            pass
        elif self.auth_key == 'v3':
            pass

        return send_request(url, method, **kwargs)

    def get_unused_phone_num(self, sql_template):
        """
        生成一个没用使用的手机号码
        :sql_template: sql模板，用来查询数据库中是否存在指定的电话号码，format风格
        例如：select id from member where mobile_phone='{}'
        :return: 手机号码
        """
        while True:
            phone_num = generate_phone_num()
            if not self.db.exist(sql_template.format(phone_num)):
                return phone_num
