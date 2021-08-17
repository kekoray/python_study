# -*- coding: utf-8 -*- 
# @Time : 2021/8/9 17:31
# @Author : koray
# @File :



# 生成器generator,是一类特殊的迭代器,性能上比迭代器好,
# 可以使用next和send取值,第一次取值时,需要用next
# 1.yield创建生成器


# 2.生成器表达式创建生成器
g = (x * 2 for x in range(5))

# ==========================

''' 可迭代对象,能被for循环遍历的对象'''
# 1.使用for循环遍历判断
List = [1, 2, 3]
str_ = "py3"
Tuple = (9, 8, 7)
Dict = {"a": 1, "b": 2, "c": 3}
Set = {"A", "B", "C"}
for i in zip(List, str_, Tuple, Dict, Set):
    print(i)

# 2.使用Iterable方法判断
from collections.abc import Iterable

print("list:", isinstance(List, Iterable))  # True
print("str:", isinstance(str_, Iterable))  # True
print("tuple:", isinstance(Tuple, Iterable))  # True
print("dict:", isinstance(Dict, Iterable))  # True
print("set:", isinstance(Set, Iterable))  # True
print("num:", isinstance(1, Iterable))  # False

'''  自定义实现可迭代对象 '''


class Iter_obj(object):
    def __init__(self, value):
        self.value = value

    # 编写迭代逻辑
    def __iter__(self):
        self.index = 3
        return iter(self.value[:self.index])


L = Iter_obj([1, 2, 3, 4, 5, 6])
print(isinstance(L, Iterable))  # True
for i in L:
    print(i)  # 只打印到索引为3,因为__iter__限制

'''  迭代器对象  '''
"""
    # 可迭代对象不是迭代器,但是迭代器是可迭代对象
    # 迭代器在for循环中遍历是不可逆的,只能遍历一次
    # 迭代器协议: 实现对象的__iter__和__next__方法
"""

# 使用Iterable方法判断
from collections.abc import Iterator

print("list:", isinstance(List, Iterator))  # False
print("str:", isinstance(str_, Iterator))  # False
print("tuple:", isinstance(Tuple, Iterator))  # False
print("dict:", isinstance(Dict, Iterator))  # False
print("set:", isinstance(Set, Iterator))  # False
print("num:", isinstance(1, Iterator))  # False

""" 创建迭代器对象 """
# 使用iter方法将可迭代对象转换为迭代器对象,且迭代器在循环遍历中是不可逆的
l = iter([1, 2])
print(isinstance(l, Iterator))  # True
next(l)  # 1
next(l)  # 2
next(l)  # StopIteration

"""  自定义实现迭代器对象  """


class IterObj(object):
    def __init__(self, value):
        self.value = value
        self.i = 0

    def __iter__(self):
        return iter(self.value)

    # 编写迭代逻辑
    def __next__(self):
        while self.i < len(self.value):
            v = self.value[self.i]
            self.i += 1
            return v
        # 此处可以增加StopIteration异常提示
        print("StopIteration...")


ite = IterObj([1, 2, 3, 4, 5])
print(isinstance(ite, Iterable))  # True
next(ite)

""" ======================  生成器对象  ==========================  """

# 定义生成器：
# 生成器generator,是一类特殊的迭代器,性能上比迭代器好,
# 可以使用next和send取值,在第一次取值时,必须使用用next,才能使用send,send会在唤醒生成器时向断点处传入一个数据

# 1.推导式创建生成器,元组不具备推导式生成,故创建的都是生成器对象
g = (x * 2 for x in range(5))
next(g)
g.send("取值成功")


# 2.使用yield创建生成器,每次会在yield的地方暂停并重新进入while,直到循环完毕了才执行return.
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1 + num2
        current += 1
        yield num
    return 'done'


g = fib(5)

while True:
    try:
        x = next(g)
        print("value:%d" % x)
    except StopIteration as e:
        print("生成器返回值:%s" % e.value)
        break
'''
value:0
value:1
value:1
value:2
value:3
生成器返回值:done
'''

""" ======================  装饰器  ==========================  """

""" ======================  闭包  ==========================  """

# 定义闭包函数：


""" ======================  装饰器  ==========================  """
# 装饰器就是两个嵌套函数返回内部函数


import time
from functools import wraps


# 定义装饰器函数,功能用于计算程序运行时间
def func(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        print('耗时：%s 秒' % (end_time - start_time))
    return inner


# 定义被装饰函数
@func
def test():
    time.sleep(2)


test()

'''带有外部参数的装饰器'''


def Decorator(name=None, level="普通会员"):
    def outer(func):
        def inner(name):
            if level == "SVIP":
                print("欢迎登陆尊贵的%s用户,过期时间还有1年" % level)
                func(name)
            else:
                print("欢迎登陆，%s" % level)
                func(name)
        return inner
    return outer


@Decorator(level="SVIP")
def func(name):
    print(name)


func("张三")

'''  在类中使用装饰器  '''


# 单例对象的创建

def singleton(cls, *args, **kw):
    instance = {}

    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
            return instance[cls]

    return _singleton


@singleton
class Singleton(object):
    def __init__(self):
        self.num_sum = 0

    def add(self):
        self.num_sum = 100


'''  类装饰器  '''


# 类方法装饰器与实例方法装饰器的调用方式不同


class Tiga(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("叮~，变身")
        self.func(*args, **kwargs)
        print("光之巨人")

    # 实例方法装饰器
    def Red(self, f):
        def wrapper(*args, **kwargs):
            print("切换战士形态：力量+100")
            f(*args, **kwargs)
        return wrapper

    # 类方法装饰器
    @classmethod
    def Blue(cls, f):
        def wrapper(*args, **kwargs):
            print("切换刺客形态：敏捷+100")
            f(*args, **kwargs)
        return wrapper


# 类装饰器调用
@Tiga
def func():
    print("化身成为光！")

# 相当于实例化的对象 func = Tiga()
func()

# 类方法装饰器的调用格式: @类名.类方法
@Tiga.Blue
def fight1():
    print("速度很快，但是没有破防")

fight1()


# 实例方法装饰器的调用格式: @对象.实例方法
@func.Red
def fight2():
    print("使出一记重拳，但是没打中")

fight2()


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
