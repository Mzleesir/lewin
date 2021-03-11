# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 10:25 下午
# @Author  : Lewin
# @FileName: day1_面向对象_07静态方法.py
# @Software: PyCharm

class Point:
    name = "点"  # 定义一个类属性

    """
    表达平面坐标系里的一个点
    """

    def __init__(self, x, y):  # 魔术方法__init__方法
        self.x = x
        self.y = y

    def __str__(self):  # 魔术方法__str__方法
        return "{}, {}".format(self.x, self.y)

    # 定义在类中的普通函数方法就是对象方法
    def my_print(self):
        print("{}, {}".format(self.x, self.y))

    def distance(self, p2):
        return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5

    @classmethod  # 类方法
    def base_point(cls):  # cls代表类本身，self代表对象本身
        bp = cls()
        bp.x = 0
        bp.y = 0
        return bp

    @staticmethod  # 静态方法
    def sum_num(x, y):
        return x + y


# 静态方法 ：在类中通过staticmethod可以把一个函数定义为静态方法
# 静态方法不会隐士的接收第一个参数，他和普通函数一样，只是被封装到类里
# 通过类或对象都可以调用

p = Point(1, 2)
res = p.sum_num(3, 4)
print(res)
