#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/16 20:48
# @Author : 心蓝
import json

json_str = '''{
    "name": "Felix",
    "age": 18,
    "hobby": ["运动","妹子",null],
    "friends": [
        {
            "name": "刘德华"
        },
        {
            "name": "梁朝伟"
        }
    ]
}
'''

# json_str - > python object
python_object = json.loads(json_str)
print(type(python_object), python_object)

# python object - > json_str

js = json.dumps(python_object, ensure_ascii=False)
print(js)
#
# None - null
print(json.dumps(None))
print(json.dumps("心蓝"))
print(json.dumps(12))
