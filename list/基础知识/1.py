# -*- coding: utf-8 -*- 
# @Time : 2021/6/22 17:11
# @Author : koray
# @File :

import requests
import sys
from math import sin as s

r = requests.get('https://www.baidu.com/')
print r.status_code
# print r.text
# print r.encoding
# print r.url

print s(3)

# =======================  数据类型  =====================================

# --------------  Numeric Type ----------------
# Numeric Type 数字类型包括有int,float,complex
# complex复数类型,由(real实部+imag虚部+虚部后缀j)组成;
# complex(real,imag)函数用于创建一个复数或者将一个数或字符串转换为复数形式,其返回值为一个复数,用c.real和c.imag来取两部分数据;
# real可以为int,long,float或字符串类型; 而image只能为int,long,或float类型; 如果第一个参数为字符串,第二个参数必须省略; 若第一个参数为其他类型,则第二个参数可以选择;

a = 2
b = 232
e = complex(float(a), float(b))
print id(a)  # 获得对象的id标识
print ['a:', type(a), 'b:', type(b), 'e:', type(e)]  # 获取当前数据的数据类型
print e  # (2+232j)
print e.real  # 2.0
print e.imag  # 232.0
