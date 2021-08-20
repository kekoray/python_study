# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# class Book:
#     # 属性为：名称name；单价price，
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         # Todo: 打印输出Python,56
#         print("{0},{1}".format(self.name, self.price))
#         '''
#              注：format()方法使用{}来做占位，拼接字符串，
#             # {}中填入索引值，{0}代表值 'World'，以此类推，这样就可以在任意位置传入任意值
#             s = 'Hello {0},Hello {1}'.format('World','Python')
#         '''
#
#
# # 实例化Book对象
# book = Book('Python', '56')


#  =========================================
#  =========================================
#  =========================================

#
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:定义一个Book类
# class Book(object):
#
#     # Todo: 属性为：名称name；单价price，
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     # 定义方法printAttr
#     def printAttr(self):
#         # Todo：打印输出book的名称和单价
#         '''
#             预期输入：
#             Python
#             56
#
#             预期输出：
#             书名-Python
#             价格-56
#
#             注：format()方法使用{}来做占位，拼接字符串，
#             # {}中填入索引值，{0}代表值 'World'，以此类推，这样就可以在任意位置传入任意值
#             s = 'Hello {0},Hello {1}'.format('World','Python')
#         '''
#         print("书名-{0}".format(self.name))
#         print("价格-{0}".format(self.price))
#
#
# # Todo: 输入两个字符串，
# name = 'Python'
# price = 56
# # Todo: 实例化Book对象，分别赋值给Book类对象的name属性和price属性
# book = Book(name, price)
# book.printAttr()

#  =========================================
#  =========================================
#  =========================================

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# class ClassA:
#     # Todo：填写 静态方法 修饰器
#     @staticmethod
#     def func_static():
#         print('staticmethod')
#
#
# class ClassB:
#     # Todo：填写 类方法 修饰器
#     @classmethod
#     def func_class(cls):
#         print('classmethod')
#
# # Todo：ClassA 静态方法 func_static()被调用
# ClassA.func_static()
#
# # Todo：ClassB 类方法 func_class()被调用
# ClassB.func_class()

#  =========================================
#  =========================================
#  =========================================

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# class Father(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Uncle(object):
#     # 在Uncle类__init__()方法中给属性name,age,weight赋值
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     # Todo:补全Child类
# class Child(Father):
#     # Todo:通过super调用父类的__init__()方法给属性name,age赋值
#     def __init__(self, name, age, ageTag):
#
#
# # Todo:给本身的属性ageTag(年代标签)赋值
# ageTag = 99
#
# # Todo:在Child类中打印输出属性的值
#
#
# # Todo:实例化Child对象
# child = Child()
#
# # Todo:通过isinstance()方法判断该对象是否是Uncle类的实例
# isinstance(child,Uncle)