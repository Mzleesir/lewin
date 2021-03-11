#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 20:23
# @Author : 心蓝
import requests

# 1. url参数，查询参数，url ?key=value&key1=value1
base_url = 'http://api.lemonban.com/futureloan'
interface_name = '/loans'
# 字典个数
args = {
    'pageIndex': 1,
    'pageSize': 10
}
url = base_url + interface_name
print(url)
# 传递给params参数的字典会自动拼接到url中
response = requests.get(url=url, params=args)
print(response.url)
print(response.text)
# 2. 拼接url  一般情况不拼接
# url = base_url + interface_name + '?pageIndex=1&pageSize=10'
#
# # 3. 发送http请求
# response = requests.get(url)
#
# print(response.text)
# # 获取请求头
# print(response.request.headers)
