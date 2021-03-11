#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/30 21:44
# @Author : 心蓝
import pymysql

# 1.创建连接
conn = pymysql.connect(
    host='api.lemonban.com',
    user='future',
    password='123456',
    db='futureloan',
    charset='utf8',
)
print(conn)
# 2.创建游标
# 传递参数cursor=pymysql.cursors.DictCursor 返回的就是列表字典结构的数据
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 3.执行sql语句
res = cursor.execute('select * from member order by id desc limit 10')
print(res)  # 返回影响的数据条数，或查询的条数
# 4.获取结果 默认情况下返回的是元组嵌套的元组
one = cursor.fetchone()  # 获取一条
print(one)
three = cursor.fetchmany(3)  # 获取三条
print(three)
rest = cursor.fetchall()  # 获取所有
print(rest)
# 5.关闭游标
cursor.close()
# 6.关闭连接
conn.close()
