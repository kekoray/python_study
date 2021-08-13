# -*- coding: utf-8 -*- 
# @Time : 2021/8/13 15:17
# @Author : koray
# @File :

# 导包
from functools import wraps


def light(func):
    print("---光--")

    # 防止装饰器导致元信息丢失
    @wraps(func)
    # 通用的装饰器参数
    def tige(*args, **kwargs):
        func(*args, **kwargs)
        print("---变身---")

    return tige


@light
def person(a, b):
    """ read me """
    print("--1号人员--", a + b)


@light
def person2():
    print("--2号人员--")


# help(person)
person(1, 2)


# person2()


# =====================================
# 通过外部参数来控制装饰器

# =====================================
# 将装饰器定义为类的形式
# __call__方法,让类像方法一样被调用

# =====================================
# 多个装饰器的使用,先执行距离主函数近的装饰器,依次类推
def a(func):
    @wraps(func)
    def a_inner():
        func()
        print("==> 执行a装饰器")
        pass

    return a_inner


def b(func):
    @wraps(func)
    def b_inner():
        func()
        print("==> 执行b装饰器")
        pass

    return b_inner


def c(func):
    @wraps(func)
    def c_inner():
        func()
        print("==> 执行c装饰器")
        pass

    return c_inner


@a
@b
@c
def P():
    print("执行P函数")


P()

# 解除装饰器,使用__wrapped__方法
p_remove = P.__wrapped__.__wrapped__.__wrapped__
p_remove()
