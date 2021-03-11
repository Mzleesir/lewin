# -*- coding: utf-8 -*-
# @Time    : 2021/2/17 12:25 上午
# @Author  : Lewin
# @FileName: json字符串.py
# @Software: PyCharm
import json
some_str = '{"name": "lewin", "age": 18}'
# 把json字符串转换成Python中的对象
res = json.loads(some_str)
print(res, type(res))

# python中的数据，保存在文本文件中
# pyobj -> json_str -> 文本文件

some_dict = {'name': 'lewin', 'age': 18}
js = json.dumps(some_dict)
print(js, type(js))

# 转文本文件
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(js)
