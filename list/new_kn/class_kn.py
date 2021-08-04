# -*- coding: utf-8 -*- 
# @Time : 2021/8/4 17:21
# @Author : koray
# @File :
from typing import Any, Iterable


class Student(object):
    # 实例的变量名如果以__开头,就是私有变量(private),避免与子类中的属性命名冲突
    # 只能内部可以访问,外部也可以使用(对象._类名__变量名)方式调用
    __addr = "china"

    def __init__(self, name, age):
        # 完全私有变量,类似private效果
        self.__name = name
        self.__age = age

    # 若要外部访问和修改变量,可以使用类似Java的get/set方法
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    # 析构方法,当实例化对象被彻底销毁时调用
    def __del__(self):
        pass

    # 定义当被len()调用时的操作
    def __len__(self):
        pass

    # 定义当被bool()调用时的操作,返回true/false
    def __bool__(self):
        pass

    # 定义当被str()调用或者print()时的操作
    # 可重写该方法,类似Java的toString方法,返回指定格式进行显示
    def __str__(self) -> str:
        return "str方法 ==> name: %s , age : %s" % (self.__name, self.__age)

    # 定义当被repr()调用或者print()时的操作
    # 可重写该方法,类似Java的toString方法,返回指定格式进行显示
    # 当类中没有str方法时,会调用repr方法,所以一般类中需要定义repr方法
    def __repr__(self) -> str:
        return "repr方法 ==> name: %s , age : %s" % (self.__name, self.__age)

    # 定义当用户试图获取一个不存在的属性时的操作
    def __getattr__(self, name):
        pass

    # 定义当一个属性被设置时的操作
    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    # 定义当该类的属性被访问时的行为
    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)


if __name__ == '__main__':
    s = Student("kk", 25)
    print(s)  # name: kk , age : 25
    print(str(s))  # name: kk , age : 25
    print(repr(s))  # repr方法 ==> name: kk , age : 25

# class Student(object):
#
#     # 类级别的静态方法,在类实例化时调用,至少传递1个参数cls
#     # 返回值必须是实例化出来的实例,即返回super(当前类名，cls).__new__(cls)
#     # 一般用于单例模式,一旦重写该方法,就要和init方法声明的参数一致
#     def __new__(cls, name, age) -> Any:
#         return super(Student, cls).__new__(cls)
#
#     # def __new__(cls) -> Any:
#     #     """
#     #     重写new方法,实例化对象取决于new方法返回什么就是什么
#     #     """
#     #     return "abc"
#
#     # 实例级别的对象初始化方法,类似构造函数,第1个参数必须是self,表示new方法返回的实例本身
#     # 若new方法没有返回当前类的cls实例,那init方法将不会被调用;
#     # 在创建实例时,必须传入与init方法声明的参数,self除外
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#
#     def print_meg(self):
#         print("name: %s , age : %s" % (self.name, self.age))
