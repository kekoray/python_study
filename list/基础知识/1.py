# -*- coding: utf-8 -*- 
# @Time : 2021/6/22 17:11
# @Author : koray
# @File :

import requests
import sys
from math import sin as s
import keyword

# r = requests.get('https://www.baidu.com/')
# print r.status_code
# print r.text
# print r.encoding
# print r.url


# =======================  数据类型  =====================================

# --------------  Numeric Type ----------------
# Numeric Type 数字类型包括有int,float,complex
# complex复数类型,由(real实部+imag虚部+虚部后缀j)组成;
# complex(real,imag)函数用于创建一个复数或者将一个数或字符串转换为复数形式,其返回值为一个复数,用c.real和c.imag来取两部分数据;
# real可以为int,long,float或字符串类型; 而image只能为int,long,或float类型; 如果第一个参数为字符串,第二个参数必须省略; 若第一个参数为其他类型,则第二个参数可以选择;

a = 2
b = 232
e = complex(float(a), float(b))
# print id(a)  # 获得对象的id标识
# print ['a:', type(a), 'b:', type(b), 'e:', type(e)]  # 获取当前数据的数据类型
# print e  # (2+232j)
# print e.real  # 2.0
# print e.imag  # 232.0


# --------------  string Type ----------------

# 定义字符串可以使用单引号,双引号,三引号等三种方式;
#
#
# 字符串输出形式
# 1. %s(字符串),%d(整型)
# 2. {0} + format()
# 3. +形式, 前后都只能是string
# 4. ,形式


# 定义字符串
_str = '123456789'

# 字符串截取:变量[开始:结束:步长],
print(_str[0:8:2])  # 输出第1个开始到第8个且每隔1个字符
print(_str[0:-1])  # 输出第1个到倒数第2个的所有字符

# 字符串内容为浮点型要转换为整型时,要先转化成float再转换成int
print(int(float("2.1")))

# 斜杠可以用来转义, 使用r可以让反斜杠不发生转义.
print('\n')  # 输出空行
print(r'\n')  # 输出 \n

#
# # 文件目录操作
# import os
# print os.getcwd()  #获取当前的文件目录结构
# os.chdir("xx/xx")  #修改当前的文件目录结构,相当于复制文件
#
#
#
#
#
#
#
# # 如何使用python来产生随机数
# # 为什么要有随机数？
# # 1）利用正态分布产生一些列的随机数，模拟现实生活中一些场景
# # 2）二项分布、beta分布
#
# #产品0-1之间的随机数
# import rendom
# print random.random() 取[0,1)内的随机小数
# print random.randint(1,10) 取[0,10]内的随机小数
# print random.randrange(1,10,2)
#
#
# # numpy包
# import numpy as np
# np.random.rendom(size(3,2)) #产生0-1之间的符合均匀分布的随机数
# #产生0-1之间的8个随机数
# np.random.randint(1,10,8)
# #产生正态分布的随机数
# pn.random.randn()
# pn.random.randn(2,4)  #参数表示矩阵size为2行4列
# #产生二项分布的随机数
# np.random.binomial(10,0.5,(2,3)) #第一个参数表示均值,二表示方差,三表示矩阵的size
# # 产生卡方分布的随机数
# np.rendom.chisquare(2,(2,3)) #第一个参数表示自由度
# #gama伽马分布
# np.random.gamma(2,4,100) #前两个参数表示自由度
#
#
