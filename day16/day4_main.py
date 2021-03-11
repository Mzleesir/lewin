# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 10:35 上午
# @Author  : Lewin
# @FileName: day4_main.py
# @Software: PyCharm
import unittest

from BeautifulReport import BeautifulReport

# # 1. 实例化一个测试套件
# ts = unittest.TestSuite()
# # 2. 收集测试
# # 一个一个的添加
# # 单元测试的语法： 测试用例类名('单元测试方法名')
# ts.addTest(TestStrUpper('test_str_upper'))
#
# # 一次添加多个
# ts.addTests([TestLogin('test_login_ok'), TestLogin('test_login_password_error')])
#
# print(ts)

# 这种方法比较笨拙

# TestLoader对象,收集器
# tloader = unittest.TestLoader()
# # 通过测试用例类名，不要加括号,需要导入
# ts = tloader.loadTestsFromTestCase(TestLogin)
# print(ts)

# 常用的方法是
tloader = unittest.TestLoader()

# discover方法
# - start_dir 开始查找的目录  递归的去所有目录下查找（目录下一定要有__init__.py)
# - pattern 查找模块名的规则  test*.py 以test开头的模块,收集里面的测试用例
# - top_level_dir 项目的顶层目录
ts = tloader.discover('.')

# 执行测试
# # 文本测试运行器实例化运行器
# runner = unittest.TextTestRunner()
# # unittest.TextTestResult()
# # 传入测试套件
# res = runner.run(ts)
# print(type(res), res)


# 1. 编写测试用例类
# 2. 收集测试用例
# 3. 运行测试，输出结果


# HTMLTestRunnerNew
from day16.HTMLTestRunnerNew import HTMLTestRunner

with open('report.html', 'wb') as f:
    runner = HTMLTestRunner(
        stream=f, description='哈哈哈哈', title='马小丹测试的', tester='马小丹')
    runner.run(ts)

# BeautifulReport
# pip install BeautifulReport
if __name__ == '__main__':
    tloader = unittest.TestLoader()
    ts = tloader.discover('.')
    # 实例化，并传入测试套件
    print(ts)
    br = BeautifulReport(ts)
    br.report('哈哈哈', 'bfreport.html')
