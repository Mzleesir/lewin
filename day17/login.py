#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/9 20:36
# @Author : 心蓝
# 目标测试函数
# 1. 分析需求
# 2. 编写测试用例
#       序号	项目	测试数据	预期结果	实际结果
#       1	账号密码正确	{"username": "python34", "password": "lemonban"}	{"code": 0, "msg": "登录成功"}
#       2	账号正确,密码错误	{"username": "python34", "password": "lemonban11"}	{"code": 1, "msg": "账号或密码不正确"}
#       3	账号错误,密码正确	{"username": "python341", "password": "lemonban"}	{"code": 1, "msg": "账号或密码不正确"}
#       4	账号正确,密码长度小于6	{"username": "python34", "password": "lemon"}	{"code": 1, "msg": "密码长度在6-18位之间"}
#       5	账号正确,密码长度大于18	{"username": "python34", "password": "lemonban12345678901"}	{"code": 1, "msg": "密码长度在6-18位之间"}
# 3. 编写测试代码
def login_check(username, password):
    """
    登录校验的函数
    :param username: 账号
    :param password: 密码
    :return:
    """
    if 6 <= len(password) <= 18:
        if username == 'python34' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "密码长度在6-18位之间"}
# __name__是模块的特殊变量
# 当直接执行当前模块的时候__name__ = '__main__'
# 当被其他模块导入的时候__name__ = 模块名
# pass 占位符，什么都不是，表示跳过


if __name__ == '__main__':
    # 这个里面的代码只有直接执行当前脚本的时候才会运行，
    # 别的代码导入当前脚本，不执行
    # 测试数据
    test_data = {"username": "python34", "password": "lemonban"}
    # 期望数据
    expect_data = {"code": 0, "msg": "登录成功"}
    if login_check(test_data['username'], test_data['password']) == expect_data:
        print('测试成功')
    else:
        print('测试失败')