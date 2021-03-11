#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 20:42
# @Author : 心蓝
import json
import requests

# 1. url参数，查询参数，url ?key=value&key1=value1
base_url = 'http://api.lemonban.com/futureloan'
interface_name = '/member/register'
url = base_url + interface_name
# 请求头字典
headers = {
    'X-Lemonban-Media-Type': 'lemonban.v1'
}
# 参数字典
data = {
    'mobile_phone': 15873061798,
    'pwd': '12345678',
}
# json参数
response = requests.post(url, headers=headers, json=data)
res = response.text
print(type(res), res)
print(json.loads(res))
# response对象有一个快捷方法,返回的的数据一定要是json格式，否则就报错
res = response.json()
print(type(res), res)

{"mobile_phone": "15873061798", "pwd": "12345678"}