# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 4:36 下午
# @Author  : Lewin
# @FileName: day2_面向对象_01复盘.py
# @Software: PyCharm

class Point():
    """
    创建一个二维平面点坐标
    """
    name = "点"

    def __init__(self, x, y):
        """
        初始化方法
        :param x:  表示一个x轴坐标
        :param y:  表示一个y轴坐标
        """
        self.x = x
        self.y = y

    def __str__(self):

        return "{}, {}".format(self.x, self.y)


point = Point(1, 2)
a = Point(3, 4)
b = Point(0, 0)
c = Point(5, 6)
print(point)
print(a)