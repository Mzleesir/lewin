#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 20:53
# @Author : 心蓝
import requests
login_url = 'https://www.ketangpai.com/UserApi/login'
args = {
    'email': '877649301@qq.com',
    'password': 'Nmbpython',
    'remember': 0
}
# form表单参数传递给形参data
response = requests.post(url=login_url, data=args)
print(response.status_code)
print(response.text)
