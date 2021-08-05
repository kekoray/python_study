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

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


if __name__ == '__main__':
    pass
