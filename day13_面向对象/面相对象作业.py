# -*- coding: utf-8 -*-
# @Time    : 2021/2/16 11:10 下午
# @Author  : Lewin
# @FileName: 面相对象作业.py
# @Software: PyCharm
"""
1. 简述如何实例化一个对象
对象名.类名（）


2. 简述如何定义类属性和对象属性
类属性：在类中使用 变量名=""
对象属性：在对象中使用 对象名=""


3. 简述对象方法的第一个参数self的含义

哪个对象调用，self就是哪个对象

4. 简述类方法的第一个参数cls的含义

表示类本身

5. 定义一个类Triangle用来表示三角形

定义类属性name表示类表示的数据

定义初始化方__init__法接收三个点作为参数（点可以用二元元组来表示，也可以使用课堂上的Point类的实例来表示，注意判断是否三个点不同）

定义__str__方法使得打印Triangle对象的字符串形式为：三角形(x,y),(x,y),(x,y)

定义方法isosceles用来判断三角形是否是等腰三角形，输出True 或False（提示，计算三个点的距离，有两个距离相等就是等腰三角形）

定义方法is_equal_sides用来判断三角形是否等边三角形，输出True或False（提示，计算三个点的距离，三个距离相等）
"""


class Triangle:
    """
    表示三角形
    """
    name = "三角形"

    def __init__(self, a, b, c):
        """

        :param a: (x, y)二元元组表示点，x, y分别表示x轴和y轴的坐标
        :param b: (x, y)二元元组表示点，x, y分别表示x轴和y轴的坐标
        :param c: (x, y)二元元组表示点，x, y分别表示x轴和y轴的坐标
        """
        if a == b or a == c or b == c:
            raise ValueError('三角形的三个点不能相同')
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return '三角形{}{}{}'.format(self.a, self.b, self.c)

    def isosceles(self):
        """
        判断三角形是否是等腰三角形
        :return:
        """
        # 计算三个边长
        d1 = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        d2 = ((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2) ** 0.5
        d3 = ((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2) ** 0.5
        if d1 == d2 or d1 == d3 or d2 == d3:
            return True
        return False

    def is_equal_sides(self):
        """
        判断三角形是否是等边三角形
        :return:
        """
        # 计算三个边长
        d1 = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        d2 = ((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2) ** 0.5
        d3 = ((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2) ** 0.5
        if d1 == d2 and d1 == d3 and d2 == d3:
            return True
        return False


if __name__ == '__main__':
    t = Triangle((1, 0), (2, 2), (3, 0))
    print(t)

    print(t.isosceles())
    print(t.is_equal_sides())
