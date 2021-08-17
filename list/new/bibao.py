# -*- coding: utf-8 -*- 
# @Time : 2021/8/13 15:17
# @Author : koray
# @File :

'''
在函数func中定义了一个inner函数, inner访问了外部函数func的变量, 并且函数返回值为inner函数
'''
def func(x):
    def inner(y):
        return x + y
    return inner
