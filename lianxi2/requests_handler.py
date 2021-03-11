# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 9:54 下午
# @Author  : Lewin
# @FileName: requests_handler.py
# @Software: PyCharm
import requests

def send_requests(url, method, **kwargs):
    """
    发送请求
    :param url:
    :param method:
    :param kwargs:
    :return:
    """
    method = method.upper()
    if method == 'GET':
        return requests.get(url, **kwargs)
    elif method == 'POST':
        return requests.post(url, **kwargs)
