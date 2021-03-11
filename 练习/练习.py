# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 10:36 上午
# @Author  : Lewin
# @FileName: 练习.py
# @Software: PyCharm
# ls = "A, b, C"

# print(ls[-1::-1])

# print(ls.replace(',', ' '))

# print(ls.capitalize())
# print(ls.casefold())
# print(ls.count('b'))
# i = 0
# for i in list(ls):
#     if ls.count(i)>1:
#         print(i + '')

# print(ls.find("c"))
# a = "The sum of 1 + 2 is {}".format(1+2)
# print(a)

# print(ls.index("d"))
# print(ls.isalnum())
# print(ls.isdigit())
# print(ls.isspace())
# print(":".join(ls))
# print(ls.lower())

# print(float(2))
# print('a, b, \tc')
# ls = ['a', 'b', 'b', 'c', [1, 2]]
# # print(ls[0])
# # # print(ls[-1][-1])
# # # ls[0] = 'd'
# # # print(ls)
# # # ls.append('f')
# # # print(ls)
# # # print(ls.count('b'))
# # ls.insert(1, 'g')
# # print(ls)
# ls.extend([3, 4])
# print(ls)
# ls.pop()
# print(ls)
# # ls.remove('b')
# # print(ls)
# print(ls.count('b'))


# a = ()                      # 空元祖
# b = ("a", "b", "cde")       # 字符串
# c = (1, "b", "c")           # 数字
# d = (1, "b", [])            # 列表
# e = (1, "b", (2, "c"))      # 元祖
# f = 1,2
#
# print('a的类型为：', type(a))    # a的类型为： <class 'tuple'>
# print('b的类型为：', type(b))    # b的类型为： <class 'tuple'>
# print('c的类型为：', type(c))    # c的类型为： <class 'tuple'>
# print('d的类型为：', type(d))    # d的类型为： <class 'tuple'>
# print('e的类型为：', type(e))    # e的类型为： <class 'tuple'>
# print('f的类型为：', type(f))    # f的类型为： <class 'tuple'>

# d = {1: 2, 'key': 'value'}
# # print(d['key'])
# d_n = {'name': "lewin", "age": 18}
# d.update(d_n)
# print(d)
# while True:
#     score = float(input("请输入你的成绩>>>:"))
#
#     if score > 60:
#         print("good")
#     else:
#         print("go_out")
# i = 0
# while i < 10:
#     print(i)
#     i += 1


# ls = ['a', 'b', 'c', 'd', 'e', 'f']
# index = 0
# while index < len(ls):
#     print(ls[index])
#     index += 1

# ls = ['a', 'b', 'c', 'd', 'e', 'f']
# for index in ls:
#     print(index)
#
# dc = {'name': 'xinlan', 'age': 18}
# for val in dc.values():
#     print(val)
# for ke in dc.keys():
#     print(ke)

# ls = [60, 59, 78, 80, 56, 55]

# for i in ls:
#     if i < 60:
#         print("stop")
#         break
# for i in ls:
#     if i > 60:
#
#         continue
#     print(i)

# try:
#     sc = input("请输入一个数值>>>:")
#     for sc in ls:
#
#         print("ok")
#     else:
#         print("no")
#
# except ValueError as e:
#     print(e)
#     print("请输入正确信息")

# try:
#     score = input('请输入你的成绩>>>:')
#     # 转换类型
#     score = float(score)
#     # 判断
#     if score < 40:
#         print('等级：E')
#     elif 40 <= score < 60:
#         print('等级：D')
#     elif 60 <= score < 75:
#         print('等级：C')
#     elif 75 <= score < 85:
#         print('等级：B')
#     else:
#         print('等级：A')
# except ValueError as e:
#     print(e)
#     print('请输入正确的成绩')
#
# else:
#     print('没有发生异常')
# finally:
#     print('我一定会执行')


# def birthday():
#     print("happy birthday to you")
#
#
# def birthday_2(name, age=18):
#     birthday()
#     birthday()
#     print("happy birthday my dear {}-{}".format(name, age))
#     birthday()
#
#
# birthday_2('lewin', 20)

# def sum_num(x, y):
#     """
#     求和
#     :param x:
#     :param y:
#     :return:
#     """
#     res = x + y
#     return res
#
#
# i = sum_num(2, 3)
# print(i)


"""
定义一个函数，它接收两个参数 content 和 times,

content 是函数要打印的内容

times 是函数打印的次数，如果不传递 times 默认打印 1 次
"""

#
# def my_print(content, times=1):
#     for i in range(times):
#         print(content)
#         times += 1
#
#
# my_print('ok', 5)

#
# def function(a, *args):
#     print(*args)
#
#
# function(1, 2, 3, 4)

# a = 1
# b = 2


# def func(a, **kwargs):
#     print(kwargs, type(kwargs))
#
#
#
#
# func(a=1, b=2, c=3, d=4)


# 定义一个函数实现打印一个数的 n 次幂。

# def func(x, n):
#     print(x**n)
#
#
# func(2, 3)


# def fun(a, b, *arg):
#     print(a, b, arg)
#
#
# ls = [1, 2, 3, 4, 5, 6]
# fun(*ls)  # => fun(1,2,3,4,5,6)
#
#
# def fun(**kwargs):
#     print(kwargs)
#
#
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# fun(**d)  # => fun(a=1,b=2,c=3,d=4)

#
# def sum_num(a, b, *args):
#     a += b
#     for i in args:
#         a = a + i
#
#     return a
#
#
# res = sum_num(1, 2, 3, 4)
#
# print(res)


# a = 1  # 全局变量
#
#
# def fun():
#     print(a)
#
#
# fun()
# print(1,2,3,sep='-',end="")
# print(1,2,3)

# print(dir('1'))

# ls = "a, b, c"
# print(ls.upper())
# print(len(ls))
#
# print(hash('1'))

# print(range(0, 10, 2))


# class Point:
#     """
#     表示平面坐标系的一个点
#     """
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "{}, {}".format(self.x, self.y)
#
#     def distance(self, p2):
#         return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5
#
#
# p1 = Point(0, 0)
# p2 = Point(1, 2)
# print(p1.distance(p2))

#
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
#
#
# t = Test()
# t.prt()


# 类定义
# class people:
#     # 定义基本属性
#     # name = ''
#     # age = 0
#     # # 定义私有属性,私有属性在类外部无法直接进行访问
#     # __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 单继承示例
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
#
# # 实例化类
# p = student('lewin', 18, 20, 6)
# p.speak()


# def func():
#     pass
# print(type(func))

# a = [ 1,2,3,4,5 ]
# print(a[:])
# print(a[-1:])
# print(a[:100])

# def f(): pass
#
# print(type(f()))

# if None:
#     print("“Hello”")

# for i in [1, 0]:
#     print(i+1)

# x = True
# y = False
# z = False
# print(y or z and x)
# print(x or y and z)

"""def Foo(x):
    if (x==1):
        return 1
    else:
        res = x+Foo(x-1)
        return res

print(Foo(4))"""


# sum_num = lambda x: x, [1, 3, 6]
# print(sum_num("1"))

# 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2
#     print("函数内 : ", total)
#     return total
#
#
# # 调用sum函数
# total = sum(10, 20)
# print("函数外 : ", total)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "{},{}".format(self.x, self.y)
#
#     def distance(self, p2):
#         return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5
#
#     def my_print(self):
#         print('({},{})'.format(self.x, self.y))
#
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# # p1.x = 1
# # p1.y = 2
# # p2.x = 3
# # p2.y = 4
# # # res = distance(p1, p2)
# # # print(res)
# # p1.my_print()
# # print(p1.distance(p2))
# p1.my_print()
# print(p1.distance(p2))
# print(p1)
# print(p2)
#
# class Animal:
#     def bark(self):
#         print('嗷嗷叫！')
#
# class Dog(Animal):
#     def bark(self):
#         print('汪汪叫！')
#
# class Cat(Animal):
#     def bark(self):
#         print('喵喵叫！')
#
# class Duck(Animal):
#     def bark(self):
#         print('嘎嘎叫！')
#
# dog = Dog()
# cat = Cat()
# duck = Duck()
# # bark(dog)
# # bark(cat)
# # bark(duck)
# dog.bark()
# 反省
# print(isinstance(1, int))
# print(isinstance(True, float))
# ls = []
# test_data = {'username': 'python34', 'password': 'lemonban'}
# print(**test_data)

def func(*args):
    print(args)


func(1, 2, 3)
