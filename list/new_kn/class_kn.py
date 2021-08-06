# -*- coding: utf-8 -*- 
# @Time : 2021/8/4 17:21
# @Author : koray
# @File :


class Student(object):
    # 实例的变量名如果以__开头,就是私有变量(类似private),主要作用是避免与子类中的属性命名冲突
    # 只能内部可以访问,外部也可以使用(对象._类名__变量名)方式调用
    __addr = "china"

    def __init__(self, name, age):
        # 私有变量,类似private效果
        self.__name = name
        self.__age = age

    # 类似toString方法
    def __repr__(self) -> str:
        return "name: %s , age : %s , addr :%s" % (self.__name, self.__age, Student.__addr)

    # def print_meg(self, addr=__addr):
    #     print("name: %s , age : %s , addr :%s" % (self.__name, self.__age, addr))

    '''
    若要外部访问和修改私有属性,可以配合使用[@property,@属性.setter,@属性.getter],类似Java的get/set方法
    '''

    # @property: 让方法向属性一样调用
    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    # @age.setter: 设置私有属性
    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
            return self.__age
        else:
            self.__age = 18
            return self.__age

    # @age.getter: 访问私有属性
    @age.getter
    def age(self):
        return self.__age


class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        # 如果类属性__instance 的值为None,那么就创建一个对象,并且赋值为这个对象的引用
        # 保证下次调用这个方法时,能够知道之前已经创建过对象了,这样就保证了只有1个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


class Dog(Singleton):
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def eat(self, food):
        print("%s 吃%s" % (self.name, food))


class Persion(object):
    """ 说明文档 """
    pass


if __name__ == '__main__':
    # 类的所有属性(返回字典,由类的数据属性组成)
    print(Persion.__dict__)
    """{'__module__': '__main__', '__doc__': ' 说明文档 ', 
    '__dict__': <attribute '__dict__' of 'Persion' objects>, '__weakref__': <attribute '__weakref__' of 'Persion' objects>}
    """
    # 类的说明文档
    print(Persion.__doc__)  # 说明文档

    # 类名
    print(Persion.__name__)  # Persion

    # 类定义所在的模块
    print(Persion.__module__)  # __main__

    # 类的父类(返回由所有父类组成的元组)
    print(Persion.__bases__)  # (<class 'object'>,)

    # p1 = Persion()
    # p2 = Persion()
    # print(p1.get_no_of_instance())  # 2
    # print(p1.num)  # 2
    # print(p2.num)  # 2
    # print(Persion.func())  # 直接类调用  ==>  这是一个静态方法

    # p1 = Singleton(22, "kk")
    # p2 = Singleton(52, "gg")
    # print(p1)  # <__main__.Singleton object at 0x000002D13E080700>
    # print(p2)  # <__main__.Singleton object at 0x000002D13E080700>
    # print(p1 == p2)  # True
    # print(p1 is p2)  # True

    # s = Student("kk", 25)
    # print(str(s))  # name: kk , age : 25 , addr :china
    # print(s._Student__addr)  # name: kk , age : 25 , addr :china
    # p = P()
    # p2 = P()
    # print(p.num)  # 2
    # print(p2.num)  # 2
    # print(P.func())  # 这是一个静态方法

    # dog = Dog(3, "大黄")
    #
    # # 查看对象类型
    # print(type(dog))  # <class '__main__.Dog'>
    # # 判断对象是否为给定的类型
    # print(isinstance(dog, Dog))  # True
    # # 获得对象的所有属性和方法
    # print(dir(dog))  # ['__add__', '__class__', '__contains__', ...]
    #
    # # 判断对象是否有name_str的属性或者方法
    # if hasattr(dog, "eat"):
    #     # 获取对象中与name_str同名的方法或者函数
    #     eat = getattr(dog, "eat")
    #     food = "骨头"
    #     eat(food)
    #     # 为对象设置一个以name_str为名的value方法或者属性
    #     setattr(dog, "temp", "饱")
    #     print("大黄吃%s 了" % dog.temp)

# s = Student("kk", 25)
# print(str(s))  # name: kk , age : 25 , addr :china
# print(s._Student__name)  # kk
# print(s.name)  # kk
# s.age = 10
# print(s.age)  # 10
