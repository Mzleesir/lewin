# -*- coding: utf-8 -*-
# @Time    : 2021/2/14 9:58 下午
# @Author  : Lewin
# @FileName: test_unittest.py
# @Software: PyCharm

# 1.导入unittest 模块，导入被检测的函数和类
# 一般系统模块放在最上面
# 第三方模块放在系统模块下方
# 自己写的模块放在最下面

import unittest
from day15.day3_login import login_check


# 2.创建测试类，继承unittest.TestCase类


class TestLogin(unittest.TestCase):
    """
    测试登录功能
    """

    # 3.如果有初始（前置）条件和结束（后置）条件，重写脚手架（fixture）方法
    # 4.定义单元测试函数，函数名必须以test开头
    def test_login_ok(self):
        """
        账号密码正确
        :return:
        """
        # 1.测试数据
        # 测试数据
        test_data = {'username': 'python34', 'password': 'lemonban'}

        # 期望数据
        except_data = {'code': 0, 'msg': '登录成功'}

        # 2.测试步骤
        # 执行函数
        res = login_check(**test_data)  # 执行结果

        # 3.断言（判断）assert
        self.assertEqual(except_data, res)
        # 如果不相等，会抛出assertError  断言错误

    def test_login_password_error(self):
        """
        账号正确，密码错误
        :return:
        """
        # 测试数据
        test_data = {'username': 'python34', 'password': 'lemonban1'}
        except_data = {'code': 1, 'msg': '账号或密码不正确'}
        # 测试步骤
        res = login_check(**test_data)
        # 断言
        self.assertEqual(except_data, res)

    def test_login_username_error(self):
        """
        账号错误，密码正确
        :return:
        """
        # 测试数据
        test_data = {'username': 'python341', 'password': 'lemonban'}
        except_data = {'code': 1, 'msg': '账号或密码不正确'}
        # 测试步骤
        res = login_check(**test_data)
        # 断言
        self.assertEqual(except_data, res)

    def test_login_passwordlen6(self):
        """
        账号正确，密码长度小于6
        :return:
        """
        # 测试数据
        test_data = {'username': 'python34', 'password': 'lemon'}
        except_data = {'code': 1, 'msg': '密码长度在6到18位之间'}
        # 测试步骤
        res = login_check(**test_data)
        # 断言
        self.assertEqual(except_data, res)

    def test_login_passwordlen18(self):
        """
        账号正确，密码长度大于18
        :return:
        """
        # 测试数据
        test_data = {'username': 'python34', 'password': 'lemonbanlemonbanlemonban'}
        except_data = {'code': 1, 'msg': '密码长度在6到18位之间'}
        # 测试步骤
        res = login_check(**test_data)
        # 断言
        self.assertEqual(except_data, res)


# 5.调用unittest.main()来执行测试用例
if __name__ == '__main__':
    unittest.main()
