# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 9:06 下午
# @Author  : Lewin
# @FileName: day1_面相对象_05类方法.py
# @Software: PyCharm

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

    @classmethod    # 类方法
    def base_point(cls):    # cls代表类本身，self代表对象本身
        bp = cls()
        bp.x = 0
        bp.y = 0
        return bp

