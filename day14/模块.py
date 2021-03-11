# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 9:43 下午
# @Author  : Lewin
# @FileName: 模块.py
# @Software: PyCharm

# 模块就是.py文件
# import 可以调用其他模块里的定义

# 1
# import demo_sum1
# demo_sum1.sum_num(1, 2)

# 2
"""
from demo_sum1 import sum_num

res = sum_num(2, 3)
print(res)
"""

# 3
from day14.demo_sum1 import *
point(4)


