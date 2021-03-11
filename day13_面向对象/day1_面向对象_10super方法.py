# -*- coding: utf-8 -*-
# @Time    : 2021/2/11 10:07 上午
# @Author  : Lewin
# @FileName: day1_面向对象_10super方法.py
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
        bp = cls(0, 0)

        return bp

    @staticmethod  # 静态方法
    def sum_num(x, y):
        return x + y


# 类的继承
# 从现有的类继承，新的类称为之类（Subclass），被继承的类称为父类、基类或者超类
# 之类可以继承父类的属性和方法

"""
案例：创建一个类表示三维的点
"""


# 重写
# 在之类中定义同名的方法和属性，会覆盖父类的方法和属性,称为重写
class TdPoint(Point):
    """
    表示三维的点
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)

    # super 方法
    def distance(self, p2):
        # ds_2 = ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5
        # ds_2 = Point.distance(self, p2)
        ds_2 = super().distance(p2)
        ds_3 = ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2 + (self.z - p2.z) ** 2) ** 0.5
        return ds_2, ds_3


tp1 = TdPoint(1, 2, 3)
tp2 = TdPoint(2, 3, 4)
res = tp1.distance(tp2)
print(res)
