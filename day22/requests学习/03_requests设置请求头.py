#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 20:38
# @Author : 心蓝
import requests

# 1. url参数，查询参数，url ?key=value&key1=value1
base_url = 'http://api.lemonban.com/futureloan'
interface_name = '/loans'
# 查询参数字典
args = {
    'pageIndex': 1,
    'pageSize': 10
}
url = base_url + interface_name
# 请求头字典
headers = {
    'X-Lemonban-Media-Type': 'lemonban.v1'
}
# 传递字典给headers参数，可以添加自定义的请求头
response = requests.get(url=url, params=args, headers=headers)
print(response.text)
print(response.request.headers)