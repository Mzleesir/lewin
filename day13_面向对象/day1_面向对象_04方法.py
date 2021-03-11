# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 8:27 下午
# @Author  : Lewin
# @FileName: day1_面向对象_04方法.py
# @Software: PyCharm

# 方法  定义在类中的函数称之为方法
# 通过调用方式的不同，分为：对象方法，类方法，静态方法，魔术方法

class Point:
    name = "点"  # 定义一个类属性

    """
    表达平面坐标系里的一个点
    """
    # 定义在类中的普通函数方法就是对象方法
    def my_print(self):
        print("{}, {}".format(self.x, self.y))

    def distance(self, p2):
        return ((self.x - p2.x)**2 + (self.y - p2.y)**2)**0.5


p = Point()
p.x = 1
p.y = 2
p.my_print()


p2 = Point()
p2.x = 0
p2.y = 0

res = p.distance(p2)
print(res)