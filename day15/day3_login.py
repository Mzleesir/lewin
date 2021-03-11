# -*- coding: utf-8 -*-
# @Time    : 2021/2/14 5:54 下午
# @Author  : Lewin
# @FileName: day4_login.py
# @Software: PyCharm

def login_check(username, password):
    """
    登录校验的函数
    :param username: 账号
    :param password: 密码
    :return:
    """
    if 6 <= len(password) <= 18:
        if username == 'python34' and password == 'lemonban':
            return {'code': 0, 'msg': '登录成功'}
        else:
            return {'code': 1, 'msg': '账号或密码不正确'}

    else:
        return {'code': 1, 'msg': '密码长度在6到18位之间'}


# __name__是模块的特殊变量
# 当直接执行当前模块儿的时候，__name__ = __main__
# 当被其他模块导入的时候，__name__ = 模块名
# pass叫占位符，表示跳过

# print(__name__)
if __name__ == '__main__':
    # 这个里面的代码只有直接执行当前脚本的时候才会执行
    # 别的代码导入当前脚本，不会被执行
    # print(__name__)

    # 测试数据
    test_data = {'username': 'python34', 'password': 'lemonban'}

    # 期望数据
    except_data = {'code': 0, 'msg': '登录成功'}

    if login_check(test_data['username'], test_data['password']) == except_data:
        print('测试成功')

    else:
        print('测试失败')



