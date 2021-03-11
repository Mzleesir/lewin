#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 20:13
# @Author : 心蓝
import requests

"""
1. url
查询参数
2. 请求方法
3. 请求头
4. 请求体
body里的参数
"""
# 各种http请求方法对应的方法
# requests.get()
# requests.post()
# requests.head()
# requests.options()
# requests.put()
# requests.delete()
response = requests.get(url='https://www.baidu.com')
# response是返回的响应
# 状态码
print(response.status_code)

# 获取响应数据
# content是原始的二进制数据
# print(response.content)
# text的属性是文本数据
# encoding属性可以获取和设置字符编码
print(response.encoding)
response.encoding = 'utf-8'
print(response.text)

# headers属性获取响应头
print(response.headers)

# url
print(response.url)



