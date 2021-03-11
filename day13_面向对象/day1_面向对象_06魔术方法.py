# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 9:49 下午
# @Author  : Lewin
# @FileName: day1_面向对象_06魔术方法.py
# @Software: PyCharm

# 魔术/特殊方法就是有特殊功能的方法，都是以双下划线开头

class Point:
    name = "点"  # 定义一个类属性

    """
    表达平面坐标系里的一个点
    """

    def __init__(self, x, y):    # 魔术方法__init__方法
        # self.属性 = 形参
        self.x = x
        self.y = y

    def __str__(self):       # 魔术方法__str__方法
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


# __init__   初始化方法，对象属性一般定义在这里
# 当创建对象的时候它会被自动调用，创建的对象会被传递给第一个参数,会接收类名括号里传入的参数,从第二个参数开始传
p = Point(1, 2)
p.my_print()

p3 = Point(2, 3)
res = p.distance(p3)
print(res)


# __str__  print一个对象的时候，实际上会调用这个对象的__str__方法，打印这个方法的返回值
print(p)