# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 10:38 上午
# @Author  : Lewin
# @FileName: day1_面向对象_12私有化.py
# @Software: PyCharm

# python 中没有那种权限仅从一个对象内部访问的私有变量
# 在Python中以一个下划线开头的名称（例如_spam）
# 应当被看作是私有

class A:
    _args = "A"

    def _method(self):
        print("我是一个私有化方法")


a = A()
print(a._args)

a._method()

# 还有一种方式是仅仅以双下划线开头

