# -*- coding: utf-8 -*- 
# @Time : 2021/8/4 17:21
# @Author : koray
# @File :


class Student(object):

    def __init__(self, *args):
        self.__name = args[0]
        self.__age = args[1]
        self.number = args

    # 定义当被len(对象)调用时的操作,获取实例对象传入参数的个数,返回值为int类型
    # 若有私有属性,最好定义__len__方法
    def __len__(self):
        print("获取 %s 类传入参数的个数" % __class__.__name__)
        return len(self.number)

    # 定义当被bool(对象)调用时的操作,返回值为True/False
    # 当该对象参与任何真值判断时,都会先调用该方法,但除了bool(对象.属性)方式外
    def __bool__(self):
        print("判断age是否大于18岁")
        return True if self.__age > 18 else False

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


class Animal(object):
    def run(self):
        print("runing...")


'''继承的体现,重写父类的方法'''


class cat(Animal):
    def run(self):
        print("%s runing..." % __class__.__name__)


def run_twice(animal_name):
    animal_name.run()


if __name__ == '__main__':
    c = []
    # 查看对象类型
    print(type(c))  # <class 'list'>

    # 判断对象是否为给定的类型
    print(isinstance(c, tuple))  # False

    # 获得对象的所有属性和方法
    print(dir(c))  # ['__add__', '__class__', '__contains__', ...]

    # 判断对象是否有给定的属性名
    print(hasattr(c, "__class__"))  # True

    # c.run()  # cat runing...
    #
    # '''多态的体现'''
    # run_twice(Animal())  # runing...
    # run_twice(c)  # cat runing...

    # s = Student("kk", 22, "china")
    # print(len(s))  # 获取类的传入参数个数  ==>  3
    # print(len(s.get_name()))  # 获取该元素的字符长度  ==>  2
    # print(bool(s))  # 判断age是否大于18岁  /  True
    # if s: print("oooo")  # 判断age是否大于18岁

# 若要外部访问和修改变量,可以使用类似Java的get/set方法
# def get_name(self):
#     return self.__name
#
# def get_age(self):
#     return self.__age
#
# def set_name(self, name):
#     self.__name = name
#
# def set_age(self, age):
#     self.age = age

# 析构方法,定义当被del(对象)调用时的操作,销毁对象并释放其空间,程序结束时会自动调用该方法
# 手动调用时,只有当对象引用为0的时候才会被调用,否则del(对象)删除的是对象的引用
# 自定义del方法的实例无法被Python循环垃圾收集器收集,所以尽量不要自定义重写del方法
# def __del__(self):
#     print("销毁对象 : %s" % self)
#
# # 删除属性的方法,定义当被del(属性)调用时的操作
# def __delattr__(self, name: str) -> None:
#     print("删除%s属性" % name)
#     # 重写方法时必须带有,避免无限递归
#     super().__delattr__(name)

# 定义当被str()调用或者print()时的操作
# 可重写该方法,类似Java的toString方法,返回指定格式进行显示
# def __str__(self) -> str:
#     return "str方法 ==> name: %s , age : %s" % (self.__name, self.__age)

# 定义当被repr()调用或者print()时的操作
# 可重写该方法,类似Java的toString方法,返回指定格式进行显示
# 当类中没有str方法时,会调用repr方法,所以一般类中需要定义repr方法
# def __repr__(self) -> str:
#     return "repr方法 ==> name: %s , age : %s" % (self.__name, self.__age)

# 定义当用户访问一个不存在的属性时的操作
# # 一般访问不存在属性时会抛出异常,重写该方法对异常进行自定义提示
# def __getattr__(self, name):
#     print("获取不到该属性")
#     return "Can't find the attribute ..."
#
# # 定义当一个属性被设置值时的操作
# # 在实例化调用init方法给对象初始化赋值时,也会调用该方法
# def __setattr__(self, name: str, value: Any) -> None:
#     print("对 %s 设置属性值为 %s" % (name, value))
#     # 重写方法时必须有其一种方式,避免无限递归情况,也可以使用 self.__dict__[name] = value
#     super().__setattr__(name, value)
#
# # 属性访问拦截器,定义当该类的属性被访问时的行为
# # 每次访问属性时都会被调用1次,若直接用(类名.类属性)形式调用类属性,是不会调用该方法
# # 一般用于查看权限、打印log日志等
# def __getattribute__(self, name: str) -> Any:
#     print("开启属性访问拦截器..")
#     if name == "name":
#         print("开始调用name属性")
#     elif name == "age":
#         print("开始调用age属性")
#     else:
#         print("开始调用其他属性")
#     # 重写方法时必须返回相应的属性,避免无限递归和调用属性失败的情况
#     return super().__getattribute__(name)


# t = s
# print(s)  # <__main__.Student object at 0x0000021A1F38C670>
# print(t)  # <__main__.Student object at 0x0000021A1F38C670>
# print(s.age)  # name: kk , age : 25
# del (s.age)  # 删除age属性
# print(s.age)  # Can't find the attribute ...
# del (t)  # 删除对象的引用,没有调用__del__方法
# del (s)  # 对象引用为0时调用__del__方法  ==>  销毁对象 : <__main__.Student object at 0x00000215107FC670>
# '''
# 程序执行完毕后,也会自动调用__del__方法,销毁s的实例化对象
# 销毁对象 : <__main__.Student object at 0x000002CEC612C280>
# '''

# print(s.age)  # 开启属性访问拦截器..  /  开始调用age属性  /  25
# s.age = 100  # 对 age 设置属性值为 100
# print(s.age)  # 开启属性访问拦截器..  /  开始调用age属性  /  100
# print(s.addr)  # 开启属性访问拦截器..  /  开始调用其他属性  /  Can't find the attribute ...
# print(Student.country)  # china

# print(str(s))  # name: kk , age : 25
# print(repr(s))  # repr方法 ==> name: kk , age : 25

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
