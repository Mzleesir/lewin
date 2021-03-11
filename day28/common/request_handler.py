#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 21:41
# @Author : 心蓝
import requests


def send_request(url, method='GET', **kwargs):
    """
    发送请求
    :param url:
    :param method:请求方法
    :param kwargs: 接收requests原生请求的关键字参数
    :return: 响应对象
    """
    method = method.upper()
    if method == 'GET':
        res = requests.get(url, **kwargs)
    elif method == 'POST':
        res = requests.post(url, **kwargs)
    elif method == 'PATCH':
        res = requests.patch(url, **kwargs)

    # 5xx 服务器错误
    if res.status_code >= 500:
        raise ValueError('服务器错误')
    elif res.status_code >= 400:
        # 4xx 客户错误
        raise ValueError('客户端错误')
    return res



if __name__ == '__main__':
    url = 'http://www.baidu.com'
    headers = {'my_headers': 'aaa'}
    send_request(url=url, method='get', headers=headers)