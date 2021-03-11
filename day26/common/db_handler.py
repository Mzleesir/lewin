#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/2 20:13
# @Author : 心蓝
import pymysql

import settings


class DB:
    def __init__(self, **kwargs):
        self.conn = pymysql.connect(**kwargs)
        self.cursor = self.conn.cursor()

    def exist(self, sql):
        """
        查询是否存在数据
        :param sql: 需要执行的sql
        :return:
        """
        self.cursor.execute(sql)
        if self.cursor.fetchone():
            return True
        return False

    def get_one(self, sql):
        """
        获取一条查询结果
        :param sql:
        :return:
        """

        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_many(self, sql, num):
        """
        获取指定条数的查询结果
        :param sql:
        :param num: 指定条数 整数
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchmany(num)

    def get_all(self, sql):
        """
        获取所有的查询结果
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_count(self, sql):
        """
        获取查询数据 条数
        :param sql:
        :return:
        """
        return self.cursor.execute(sql)

    def __del__(self):
        # 析构方法
        self.cursor.close()
        self.conn.close()


db = DB(**settings.DATABASE_CONFIG)

if __name__ == '__main__':
    db = DB(
    host='api.lemonban.com',
    user='future',
    password='123456',
    db='futureloan',
    charset='utf8',
    )

    # res = db.get_one('select * from member order by id desc limit 1')
    # print(res)
    # res = db.exist("select id from member where mobile_phone='157'")
    # print(res)
    res = db.cursor.execute('SELECT id FROM `member` WHERE mobile_phone="phone" and `type`=0 and reg_name="美丽可爱的小简"')
    print(res)
    print(db.cursor.fetchone())



