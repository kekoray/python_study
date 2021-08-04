# -*- coding: utf-8 -*- 
# @Time : 2021/8/4 17:21
# @Author : koray
# @File :
from typing import Any


class Student(object):
    # 在Python中，实例的变量名如果以__开头,就变成了一个私有变量(private),只有内部可以访问,外部不能访问
    __addr = "china"

    # __init__方法的第一个参数永远是self,表示创建的实例本身;在创建实例的时候,必须传入与init方法匹配的参数,self不需要传
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_meg(self, addr=__addr):
        print("%s,%s,%s" % (self.__name, self.__age, addr))

    # 类似Java的get/set方法
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


if __name__ == '__main__':
    s = Student("kk", "25")
    s.print_meg()
