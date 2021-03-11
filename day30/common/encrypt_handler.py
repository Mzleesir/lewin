#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2020/11/24 下午2:30
# @Author  : superfan
import rsa
import base64
from time import time

"""
rsa 文档：https://stuvel.eu/python-rsa-doc/index.html
RSA加密：http://www.lemfix.com/topics/355(来自柠檬班 - 木森)

调用接口加密处理参考方案：
https://www.cnblogs.com/Simple-Small/p/11284110.html

测试小白也能懂：常用加密算法解析
http://www.lemfix.com/topics/43408
"""


def rsa_encrypt(msg):
    """
    公钥加密
    :param msg: 要加密的内容
    :type msg: str
    :return: 加密之后的密文
    """
    server_pub_key = """
    -----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
    O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
    tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
    kKlZFc8Br7SHtbL2tQIDAQAB
    -----END PUBLIC KEY-----
    """

    # 生成公钥对象
    pub_key_byte = server_pub_key.encode("utf-8")
    # print(pub_key_byte)
    pub_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_byte)
    print(pub_key_obj,'------------------------')

    # 要加密的数据转成字节对象
    content = msg.encode("utf-8")

    # 加密,返回加密文本
    crypt_msg = rsa.encrypt(content, pub_key_obj)
    # base64编码
    cipher_base64 = base64.b64encode(crypt_msg)
    # 转成字符串
    return cipher_base64.decode()


def generator_sign(token):
    # 获取token的前50位
    token_50 = token[:50]
    # 生成时间戳
    timestamp = int(time())
    # print(timestamp)
    # 接拼token前50位和时间戳
    msg = token_50 + str(timestamp)
    # print(msg)
    # 进行RSA加密
    sign = rsa_encrypt(msg)
    return sign, timestamp


if __name__ == '__main__':
    import requests
    # lemon_v3测试
    headers = {"X-Lemonban-Media-Type": "lemonban.v3",
               "Content-Type": "application/json"}

    # 登陆接口
    login_url = "http://api.lemonban.com/futureloan/member/login"
    login_datas = {"mobile_phone": "15088314689", "pwd": "123456789"}
    resp = requests.request("POST", login_url, json=login_datas, headers=headers)
    resp = resp.json()
    token = resp["data"]["token_info"]["token"]
    member_id = resp["data"]["id"]

    headers["Authorization"] = "Bearer {}".format(token)
    sign, timestamp = generator_sign(token)
    print("签名为： ", sign, "\n时间戳为： ", timestamp)

    recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    recharge_data = {"member_id": member_id, "amount": 2000, "sign": sign, "timestamp": timestamp}
    resp = requests.request("POST", recharge_url, json=recharge_data, headers=headers)
    print(resp.json())
    # 充值接口