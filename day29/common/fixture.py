#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/7 20:42
# @Author : 心蓝
import settings
from common.request_handler import send_request
from common.log_handler import logger


def register(mobile_phone, pwd, type_=1):
    """
    注册一个用户
    :param mobile_phone:
    :param pwd:
    :param type_: 类型 1 普通用户 0 管理员账号
    :return:
    """
    data = {
        'mobile_phone': mobile_phone,
        'pwd': pwd,
        'type': type_
    }
    url = settings.PROJECT_HOST + settings.INTERFACE['register']
    headers = settings.CUSTOM_HEADERS['v1']
    res = send_request(url, method='POST', json=data, headers=headers).json()
    logger.info('注册用户: {}'.format(data))
    if res['code'] == 0:
        return True
    raise RuntimeError('错误信息：{}'.format(res))


def login(mobile_phone, pwd):
    """
    登录
    :param mobile_phone:
    :param pwd:
    :return:
    """
    data = {
        'mobile_phone': mobile_phone,
        'pwd': pwd
    }
    url = settings.PROJECT_HOST + settings.INTERFACE['login']
    headers = settings.CUSTOM_HEADERS['v2']
    logger.info('登录用户：{}'.format(data))
    res = send_request(url, method='POST', json=data, headers=headers).json()
    if res['code'] == 0:
        return res['data']
    raise RuntimeError('错误信息:{}'.format(res))


def recharge(member_id, amount, token):
    """
    充值
    :param member_id:
    :param amount:
    :param token:
    :return:
    """
    data = {
        'member_id': member_id,
        'amount': amount
    }
    url = settings.PROJECT_HOST + settings.INTERFACE['recharge']
    # 鉴权
    headers = {'authorization': 'Bearer '+token}
    headers.update(settings.CUSTOM_HEADERS['v2'])

    logger.info('给用户{member_id}充值{amount}'.format(**data))
    res = send_request(url, method='POST', json=data, headers=headers).json()
    if res['code'] == 0:
        return res['data']
    raise RuntimeError('错误信息:{}'.format(res))


def add_loan(member_id, token, title='借钱实现财富自由', amount=5000, loan_rate=12.0, loan_term=3, loan_date_type=1, bidding_days=5):
    data = {
        'member_id': member_id,
        'title': title,
        'amount': amount,
        'loan_rate': loan_rate,
        'loan_term': loan_term,
        'loan_date_type': loan_date_type,
        'bidding_days': bidding_days,
    }
    url = settings.PROJECT_HOST + settings.INTERFACE['add']
    logger.info('用户{}加标借钱{}'.format(member_id, amount))
    headers = {'authorization': 'Bearer ' + token}
    headers.update(settings.CUSTOM_HEADERS['v2'])
    res = send_request(url=url, method='post', json=data, headers=headers).json()
    if res['code'] == 0:
        return res
    raise RuntimeError('用户加标失败,错误信息:{}'.format(res))



if __name__ == '__main__':
    # res = register('15888888888', '12345678')
    # print(res)

    res = login('15888888888', '12345678')
    print(res)
    res = recharge(member_id=res['id'], amount=800, token=res['token_info']['token'])
    print(res)