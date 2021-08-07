# -*- coding: utf-8 -*- 
# @Time : 2021/8/5 18:25
# @Author : koray
# @File :  建类模板


class Testmd(object):

    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def __repr__(self) -> str:
        return "name : %s , age : %s" % (self.__name, self.__age)

    def __getattr__(self, name):
        return "Can't find the attribute ..."

    @property
    def age(self):
        return self.__age

    # 设置属性
    @age.setter
    def age(self, age):
        self.__age = age
        return self.__age

    @age.getter
    def age(self):
        return self.__age


if __name__ == '__main__':
    pass
