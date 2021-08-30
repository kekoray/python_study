# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Tower类
# class Tower(object):
#     # Todo:初始化属性name, location, AD, ADSpace攻击间隔默认2秒钟
#     def __init__(self, name, location, AD, ADSpace=2):
#         self.name = name
#         self.location = location
#         self.AD = AD
#         self.ADSpace = ADSpace
#         # Todo:在Tower类中打印输出属性的值
#         print("Tower:%s,%s,%d,%d" % (self.name, self.location, self.AD, self.ADSpace))
#
#
# # Todo: 输入三行字符，按照顺序依次为对象的名称(name)、位置(location)、攻击力(AD)初始化、攻击间隔默认2秒钟
# name = '防御塔'
# location = '前沿塔'
# AD = 200
#
# # Todo:实例化Tower对象,打印输出结果
# Tower(name, location, AD)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# import random
#
# # Todo:补全Tower类
# class Tower(object):
#     # Todo:初始化属性name, location, AD, ADSpace攻击间隔默认2秒钟
#     def __init__(self, name, location, AD, ADSpace=2):
#         self.name = name
#         self.location = location
#         self.AD = AD
#         self.ADSpace = ADSpace
#         # Todo:在Tower类中打印输出属性的值
#         print("Tower:%s,%s,%d,%d" % (self.name, self.location, self.AD, self.ADSpace))
#
#     # Todo:  补全attack()方法，
#     #       传入参数为：攻击目标的生命值，
#     #       返回值：攻击目标的剩余生命值。
#     def attack(self, number):
#         result = 0
#         if number > 0:
#             result = number - self.AD
#         return result
#
#
# # Todo: 输入四行字符，按照顺序依次为Tower类对象的名称(name)、位置(location)、攻击力(AD)、攻击目标的生命值
# name = '防御塔'
# location = '前沿塔'
# AD = 120
# HP = 980
#
# # Todo:实例化Tower对象
# t = Tower(name, location, AD)
#
# # Todo:  调用attack方法，计算防御塔攻击的次数、击杀目标所消耗的时间。
# #       防御塔每攻击一次需要随机生成叠加伤害比率，在50%~60%之间浮动
# num = 0
# time = 0
# while HP > 0:
#     HP = t.attack(HP) - t.AD * (random.uniform(0.5, 0.6))
#     num += 1
#     if HP > 0:
#         time += t.ADSpace
#
# # Todo:打印输出防御塔攻击的次数、击杀目标所消耗的时间。
# print(num)
# print(time)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Hero类
# class Hero(object):
#     # Todo:初始化属性name, maxHP, maxMP, AD
#     def __init__(self, name, maxHP, maxMP, AD):
#         self.name = name
#         self.maxHP = maxHP
#         self.maxMP = maxMP
#         self.AD = AD
#         print("Tower:%s,%d,%d,%d" % (self.name, self.maxHP, self.maxMP, self.AD))
#
#     # Todo:补全getExp方法 传入参数为：被英雄攻击的【小兵】的生命值，返回值为:获得的经验值。
#     def getExp(self, HP):
#         result = 0
#         if HP > 0:
#             result = int(HP / 10)
#         return result
#
#     # Todo:补全getMoney方法 传入参数为：被英雄攻击的【小兵】的生命值，返回值为:获得的金币。
#     def getMoney(self, HP):
#         result = 0
#         if HP > 0:
#             result = int(HP / 30)
#         return result
#
#
# '''
#     #Todo:  输入五行字符，按照顺序依次为Hero类对象的名称(name)、最大生命值(maxHP)、
#             最大魔法值(maxMP)、攻击力(AD)初始化，【小兵】最大生命值。
#             根据步骤描述，完成场景设定动作，打印输出结果。
#             建议最大生命值(maxHP)、最大魔法值(maxMP)、攻击力(AD)、【小兵】最大生命值为整数。
# '''
# name ='古月之羽'
# maxHP =1000
# maxMP =500
# AD =45
# HP=800
#
# # Todo:实例化Hero对象,打印输出结果
# hero = Hero(name, maxHP, maxMP, AD)
#
# # Todo : 调用Hero类的getExp()方法，执行获取经验的动作
# e = hero.getExp(HP)
#
# # Todo:打印输出获取的经验值。
# print(e)
#
# # Todo ：调用Hero类的getMoney()方法，执行获取金币的动作
# m = hero.getMoney(HP)
#
# # Todo:打印输出获取的金币。
# print(m)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Hero类
# class Hero(object):
#     # Todo:初始化属性name, maxHP, maxMP, AD
#     def __init__(self, name, maxHP, maxMP, AD):
#         self.name = name
#         self.maxHP = maxHP
#         self.maxMP = maxMP
#         self.AD = AD
#         print("Tower:%s,%d,%d,%d" % (self.name, self.maxHP, self.maxMP, self.AD))
#
#     # Todo:补全getExp方法 传入参数为：被英雄攻击的【小兵】的生命值，返回值为:获得的经验值。
#     def getExp(self, HP):
#         result = 0
#         if HP > 0:
#             result = int(HP / 10)
#         return result
#
#     # Todo:补全getMoney方法 传入参数为：被英雄攻击的【小兵】的生命值，返回值为:获得的金币。
#     def getMoney(self, HP):
#         result = 0
#         if HP > 0:
#             result = int(HP / 30)
#         return result
#
#
# '''
#     #Todo:  输入五行字符，按照顺序依次为Hero类对象的名称(name)、最大生命值(maxHP)、
#             最大魔法值(maxMP)、攻击力(AD)初始化，【小兵】最大生命值。
#             根据步骤描述，完成场景设定动作，打印输出结果。
#             建议最大生命值(maxHP)、最大魔法值(maxMP)、攻击力(AD)、【小兵】最大生命值为整数。
# '''
# name = '古月之羽'
# maxHP = 1000
# maxMP = 500
# AD = 45
# HP = 900
#
# # Todo:实例化Hero对象,打印输出结果
# hero = Hero(name, maxHP, maxMP, AD)
#
# # Todo : 调用Hero类的getExp()方法，执行获取经验的动作，最后一击额外获得20%经验
# e = hero.getExp(HP)
# for i in range(int(HP / hero.AD)):
#     if i + 1 == int(HP / hero.AD):
#         e = int(e * (1 + 0.2))
#     else:
#         pass
#
# # Todo:打印输出获取的经验值。
# print(e)
#
# # Todo ：调用Hero类的getMoney()方法，执行获取金币的动作，最后一击额外获得20%金币
# m = hero.getMoney(HP)
# for i in range(int(HP / hero.AD)):
#     if i + 1 == int(HP / hero.AD):
#         m = int(m * (1 + 0.2))
#     else:
#         pass
#
# # Todo:打印输出获取的金币。
# print(m)


# !/usr/bin/python
# -*- coding: UTF-8 -*-

# Todo:补全Hero类
class Hero(object):
    # Todo:初始化属性name, maxHP, maxMP, AD
    def __init__(self, name, maxHP, maxMP, AD):
        self.name = name
        self.maxHP = maxHP
        self.maxMP = maxMP
        self.AD = AD
        print("Tower:%s,%d,%d,%d" % (self.name, self.maxHP, self.maxMP, self.AD))

    # Todo:补全getExp方法 传入参数为：被英雄攻击的【小兵】的生命值，返回值为:获得的经验值。
    def getExp(self, HP):
        result = 0
        if HP > 0:
            result = int(HP / 10)
        return result

    # Todo:补全getMoney方法 传入参数为：被英雄攻击的【小兵】的生命值，返回值为:获得的金币。
    def getMoney(self, HP):
        result = 0
        if HP > 0:
            result = int(HP / 30)
        return result


'''
    #Todo:  输入七行字符，
            按照顺序依次为Hero类对象的名称(name)、最大生命值(maxHP)、最大魔法值(maxMP)、
            攻击力(AD)初始化，两个【小兵】最大生命值，B英雄的生命值
            建议最大生命值(maxHP)、最大魔法值(maxMP)、攻击力(AD)、【小兵】最大生命值、B英雄的生命值为整数。
'''
name = '古月之羽'
maxHP = 1000
maxMP = 500
AD = 45

hHP = 900
b1HP = 500
b2HP = 500

# Todo:实例化Hero对象
hero = Hero(name, maxHP, maxMP, AD)

# Todo : 调用Hero类的getExp()方法，执行获取经验的动作，击杀小兵及英雄，最后一击额外获得20%经验
e = hero.getExp(hHP)
for i in range(int(hHP / hero.AD)):
    if i + 1 == int(hHP / hero.AD):
        e = int(e * (1 + 0.2))
    else:
        pass

e += hero.getExp(b1HP)
for i in range(int(b1HP / hero.AD)):
    if i + 1 == int(b1HP / hero.AD):
        e += int(e * (1 + 0.2))
    else:
        pass

e += hero.getExp(b2HP)
for i in range(int(b2HP / hero.AD)):
    if i + 1 == int(b2HP / hero.AD):
        e += int(e * (1 + 0.2))
    else:
        pass

# Todo:打印输出获取的经验值。
print(e)

# Todo ：调用Hero类的getMoney()方法，执行获取金币的动作，最后一击额外获得20%金币
m = hero.getMoney(hHP)
for i in range(int(hHP / hero.AD)):
    if i + 1 == int(hHP / hero.AD):
        m = int(m * (1 + 0.2))
    else:
        pass

m += hero.getMoney(b1HP)
for i in range(int(b1HP / hero.AD)):
    if i + 1 == int(b1HP / hero.AD):
        m += int(m * (1 + 0.2))
    else:
        pass

m += hero.getMoney(b2HP)
for i in range(int(b2HP / hero.AD)):
    if i + 1 == int(b2HP / hero.AD):
        m += int(m * (1 + 0.2))
    else:
        pass



# Todo:打印输出获取的金币。
print(m)
