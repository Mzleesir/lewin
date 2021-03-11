# -*- coding: utf-8 -*-
# @Time    : 2021/2/11 10:20 上午
# @Author  : Lewin
# @FileName: day1_面向对象_11多态.py
# @Software: PyCharm

# python 是一门解释性语言，动态语言，不存在多态的问题

def bark(animal):
    animal.bark()


# 对于静态语言来说，传入的对象一定要是指定的数据类型，否则就报错

class Animal:
    def bark(self):
        print("嗷嗷叫")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class Cat(Animal):
    def bark(self):
        print("喵喵叫")


class Duck(Animal):
    def bark(self):
        print("嘎嘎叫")


dog = Dog()
cat = Cat()
duck = Duck()

bark(dog)
bark(cat)
bark(duck)