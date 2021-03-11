# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 6:00 下午
# @Author  : Lewin
# @FileName: test_cases.py
# @Software: PyCharm
import unittest
from day15.day3_login import login_check


# 1.导入unittest框架和模块
# 2.定义一个测试类继承unittest.TestCases类
class Test_Login(unittest.TestCase):

    # 3.定义测试函数
    def test_login_ok(self):
        """
        登录成功
        :return:
        """
        # 1.测试数据
        test_data = {'username': 'python34', 'password': 'lemonban'}
        # 期望数据
        except_data = {'code': 0, 'msg': '登录成功'}
        # 2.测试步骤
        res = login_check(**test_data)

        # 3.断言
        self.assertEqual(except_data, res)

    def test_login_pwd_error(self):
        """
        密码错误
        :return:
        """
        # 1.测试数据
        test_data = {'username': 'python34', 'password': 'lemonban1'}
        except_data = {'code': 1, 'msg': '账号或密码不正确'}
        # 2.测试步骤
        res = login_check(**test_data)

        # 3.断言
        self.assertEqual(except_data, res)

    def test_login_uesr_reeor(self):
        """
        用户名错误
        :return:
        """
        test_data = {'username': 'python341', 'password': 'lemonban'}
        except_data = {'code': 1, 'msg': '账号或密码不正确'}
        res = login_check(**test_data)
        self.assertEqual(except_data, res)


# 4.调用unittest.main()来执行测试用例


if __name__ == '__main__':
    unittest.main()
