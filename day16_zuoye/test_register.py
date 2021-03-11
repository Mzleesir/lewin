# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 3:37 下午
# @Author  : Lewin
# @FileName: test_register_by_ddt.py
# @Software: PyCharm

# 1.导入unittest 模块，导入被检测的函数和类
import unittest
from day16_zuoye.register import register


# 2.创建测试类，继承unittest.TestCase类
class TestRegister(unittest.TestCase):
    """
    测试注册功能
    """

    # 3.如果有初始（前置）条件和结束（后置）条件，重写脚手架（fixture）方法

    # 4.定义单元测试函数，函数名必须以test开头
    def test_register_ok(self):
        """
        注册成功
        :return:
        """
        # 1.测试数据
        # 测试数据
        test_data = {'username': 'python34', 'password1': '123456', 'password2': '123456'}
        # 期望数据
        except_data = {"code": 1, "msg": "注册成功"}
        # 2.测试步骤
        # 执行函数
        res = register(**test_data)
        # 3.断言（判断）assert
        self.assertEqual(except_data, res)

    def test_register_no_username(self):
        """
        用户名为空
        :return:
        """
        # 1.测试数据
        # 测试数据
        test_data = {'username': '', 'password1': '123456', 'password2': '123456'}
        # 期望数据
        except_data = {"code": 0, "msg": "所有参数不能为空"}
        # 2.测试步骤
        # 执行函数
        res = register(**test_data)
        # 3.断言（判断）assert
        self.assertEqual(except_data, res)

    def test_register_no_password(self):
        """
        密码为空
        :return:
        """
        # 1.测试数据
        # 测试数据
        test_data = {'username': 'python35', 'password1': '', 'password2': ''}
        # 期望数据
        except_data = {"code": 0, "msg": "所有参数不能为空"}
        # 2.测试步骤
        # 执行函数
        res = register(**test_data)
        # 3.断言（判断）assert
        self.assertEqual(except_data, res)

    def test_register_password_not_equal(self):
        """
        密码不同
        :return:
        """
        # 1.测试数据
        # 测试数据
        test_data = {'username': 'python35', 'password1': '123456', 'password2': '1234567'}
        # 期望数据
        except_data = {"code": 0, "msg": "两次密码不一致"}
        # 2.测试步骤
        # 执行函数
        res = register(**test_data)
        # 3.断言（判断）assert
        self.assertEqual(except_data, res)

    def test_register_username_equal(self):
        """
        用户名已存在
        :return:
        """
        # 1.测试数据
        # 测试数据
        test_data = {'username': 'python34', 'password1': '123456', 'password2': '123456'}
        # 期望数据
        except_data = {"code": 0, "msg": "该账户已存在"}
        # 2.测试步骤
        # 执行函数
        res = register(**test_data)
        # 3.断言（判断）assert
        self.assertEqual(except_data, res)

    def test_register_password_too_sort(self):
        """
        密码小于6位
        :return:
        """
        # 1.测试数据
        # 测试数据
        test_data = {'username': 'python35', 'password1': '12345', 'password2': '12345'}
        # 期望数据
        except_data = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 2.测试步骤
        # 执行函数
        res = register(**test_data)
        # 3.断言（判断）assert
        self.assertEqual(except_data, res)

    def test_register_password_too_long(self):
        """
        密码大于18位
        :return:
        """
        # 1.测试数据
        # 测试数据
        test_data = {'username': 'python35', 'password1': '12345678901234567890', 'password2': '12345678901234567890'}
        # 期望数据
        except_data = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 2.测试步骤
        # 执行函数
        res = register(**test_data)
        # 3.断言（判断）assert
        self.assertEqual(except_data, res)


# 5.调用unittest.main()来执行测试用例
if __name__ == '__main__':
    unittest.main()
