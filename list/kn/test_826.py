# #!/usr/bin/python
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
#
# # Todo:补全Child类
# class Child(Father):
#
#     # Todo:通过super调用父类的__init__()方法给属性name,age赋值
#     def __init__(self, name, age, ageTag):
#         super().__init__(name, age)
#         self.name = name
#         self.age = age
#         # Todo:给本身的属性ageTag(年代标签)赋值
#         self.ageTag = ageTag
#
#         # Todo:在Child类中打印输出属性的值
#         print("Child:%s,%d,%s" % (self.name, self.age, self.ageTag))
#
#
# # Todo:实例化Child对象
# c = Child("Tom", 14, '00s')
#
# # Todo:通过isinstance()方法判断该对象是否是Uncle类的实例
# print(isinstance(c, Uncle))

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Child类
# class Child(object):
#
#     # Todo:通过super调用父类的__init__()方法给属性name,age,wieght赋值
#     def __init__(self, name, age, wieght):
#         self.name = name
#         self.age = age
#         self.__wieght = wieght
#
#     # Todo: 打印输出对象的所有属性
#     def printmsg(self):
#         print("Child:%s,%d,%d" % (self.name, self.age, self.__wieght))
#
# # Todo:实例化Child对象
# c = Child("Tom", 14, 170)
#
# # Todo: 调用printmsg方法，打印输出结果
# c.printmsg()


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
#
# # Todo:补全Child类
# class Child(object):
#     # Todo:通过super调用父类的__init__()方法给属性name,age,wieght赋值
#     def __init__(self, name, age, wieght):
#         self.name = name
#         self.age = age
#         self.__wieght = wieght
#
#     # Todo: 打印输出对象的所有属性
#     def __printmsg(self):
#         print("Child:%s,%d,%d" % (self.name, self.age, self.__wieght))
#
#
# # Todo:实例化Child对象
# c = Child("Tom", 14, 170)
#
# # Todo: 调用printmsg方法，打印输出结果
# c._Child__printmsg()


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Hero类
# class Hero(object):
#     # Todo:初始化属性name, maxHP, maxMP
#     def __init__(self, name, maxHP, maxMP):
#         self.name = name
#         self.maxHp = maxHP
#         self.maxMp = maxMP
#         # Todo:在Hero类中打印输出属性的值
#         print("Hero:%s,%d,%d" % (self.name, self.maxHp, self.maxMp))
#
#
# # Todo: 输入三行字符，按照顺序依次为Hero类对象的名称(name)、最大生命值(maxHP)、最大魔法值(maxMP)初始化
# name = '心羽之翼'
# maxHp = 500
# maxMp = 180
#
# # Todo:实例化Hero对象,打印输出结果
# Hero(name, maxHp, maxMp)
#
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Rune类
# class Rune(object):
#     # Todo:初始化属性name, color, attribute
#     def __init__(self, name, color, attribute):
#         self.name = name
#         self.color = color
#         self.attribute = attribute
#         # Todo:在Rune类中打印输出属性的值
#         print("Rune:%s,%s,%s" % (self.name, self.color, self.attribute))
#
#
# # Todo: 输入三行字符，按照顺序依次为对象的名称(name)、颜色(color)、属性(attribute)初始化
# name = "地狱"
# color = "蓝色"
# attribute = "最大生命+45"
#
# # Todo:实例化Rune对象,打印输出结果
# Rune(name, color, attribute)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Tower类
# class Tower(object):
#     # Todo:初始化属性name, location, attack
#     def __init__(self, name, location, attack):
#         self.name = name
#         self.location = location
#         self.attack = attack
#         # Todo:在Rune类中打印输出属性的值
#         print("Tower:%s,%s,%d" % (self.name, self.location, self.attack))
#
#
# # Todo: 输入三行字符，按照顺序依次为对象的名称(name)、位置(location)、攻击力(attack)初始化
# name = "防御塔"
# location = "一塔"
# attack = 200
# # Todo:实例化Tower对象,打印输出结果
# Tower(name,location,attack)


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
#         print("Hero:%s,%d,%d,%d" % (self.name, self.maxHP, self.maxMP, self.AD))
#
#     # Todo:补全attack方法 传入参数为：被英雄攻击的怪物的生命值，返回值为:被英雄攻击后，怪物的剩余生命值。
#     def attack(self, HP):
#         result = 0
#         while HP > 0:
#             HP -= self.AD
#             result += 1
#         return result
#
#
# '''
#     #Todo:  输入五行字符，按照顺序依次为Hero类对象的名称(name)、
#             最大生命值(maxHP)、最大魔法值(maxMP)、攻击力(AD)初始化，怪物最大生命值。
#             建议最大生命值(maxHP)、最大魔法值(maxMP)、攻击力(AD)、怪物最大生命值为整数
# '''
# name = "古月之羽"
# maxHp = 1000
# maxMp = 500
# AD = 45
# HP = 800
# # Todo:实例化Hero对象,打印输出结果
# h = Hero(name, maxHp, maxMp, AD)
#
# '''
#     #Todo : 调用Hero类的attack()方法，执行攻击动作，计算击杀当前怪物需要攻击几次。
#             友情提示：英雄反复攻击怪物，怪物生命值小于等于0，则停止攻击，计数器停止计数
# '''
#
# # Todo: 打印输出需要攻击的次数。
# print(h.attack(HP))


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Hero类
# class Hero(object):
#     # Todo: 初始化属性name、AD、maxEXP、currentEXP,升级所需经验值(maxEXP)默认为100、当前经验值(currentEXP)默认为0
#     def __init__(self, name, AD, maxEXP=100, currentEXP=0):
#         self.name = name
#         self.AD = AD
#         self.maxEXP = maxEXP
#         self.currentEXP = currentEXP
#         print("Hero:%s,%d,%d,%d" % (self.name, self.AD, self.maxEXP, self.currentEXP))
#
#     # attack方法，传入参数为：被英雄攻击的怪物的生命值，返回值为:被英雄攻击后，怪物的剩余生命值。
#     def attack(self, HP):
#         result = 0
#         if HP > 0:
#             result = HP - self.AD
#         return result
#
#     # Todo:补全isKilled方法，传入参数为：击杀的怪物的生命值，返回值为:击杀该怪物，英雄应该获得的经验值。怪物每10点生命值，英雄获取1点经验值。
#     def isKilled(self, HP):
#         result = 0
#         if HP > 0:
#             result += int(HP / 10)
#         return result
#
#
# '''
#     #Todo:  输入三行字符，按照顺序依次为Hero类对象的名称(name)、
#             攻击力(AD)、怪物的生命值初始化
# '''
# name = "古月之羽"
# AD = 45
# HP = 800
# # Todo:实例化Hero对象,打印输出结果
# h = Hero(name, AD)
#
# '''
#     #Todo : 调用Hero类的attack()方法，执行攻击动作，最终击杀怪物，调用isKilled方法返回英雄当前的经验值，打印输出。
#             友情提示：英雄一直攻击怪物，怪物生命值小于等于0，则停止攻击。
# '''
# # Todo: 调用Hero类的isKilled()方法, 计算英雄获取的经验值
# eper = h.isKilled(HP)
# # Todo: 打印输出当前Hero对象的经验值
# print(eper)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Hero类
# class Hero(object):
#
#     # Todo:  初始化属性name、AD、maxEXP、currentEXP，升级所需经验值(maxEXP)默认为100、
#     #       当前经验值(currentEXP)默认为0、英雄当前等级(currentLevel)默认为1
#     def __init__(self, name, AD, maxEXP=100, currentEXP=0, currentLevel=1):
#         self.name = name
#         self.AD = AD
#         self.maxEXP = maxEXP
#         self.currentEXP = currentEXP
#         self.currentLevel = currentLevel
#         print("Hero:%s,%d,%d,%d,%d" % (self.name, self.AD, self.maxEXP, self.currentEXP, self.currentLevel))
#
#     # Todo:  补全isKilled方法，
#     #       传入参数为：击杀的怪物的生命值，
#     #       返回值为:击杀该怪物，英雄应该获得的经验值。
#     #       怪物每10点生命值，英雄获取1点经验值。
#     def isKilled(self, HP):
#         result = 0
#         if HP > 0:
#             result += int(HP / 10)
#         return result
#
#     # Todo:  补全changeExp()方法，
#     #       传入参数为：英雄应该获得的经验值，
#     #       返回值为：英雄提升等级数值。
#     #       默认英雄击杀一个怪物最多提升一个等级
#
#     def changeExp(self, exp):
#         result = self.currentLevel
#         if self.maxEXP <= exp:
#             result += 1
#         return result
#
#
# '''
#     #Todo:  输入三行字符，按照顺序依次为Hero类对象的名称(name)、
#             攻击力(AD)、怪物的生命值初始化
# '''
#
# name = "古月之羽"
# AD = 45
# HP = 800
# # Todo:实例化Hero对象,打印输出结果
# h = Hero(name, AD)
#
# # Todo: 调用Hero类的isKilled()方法, 计算英雄获取的经验值
# exp = h.isKilled(HP)
#
# # Todo: 调用Hero类的changeExp()方法, 修改英雄经验值及等级状态
# level = h.changeExp(exp)
#
# # Todo: 打印输出英雄当前等级。
# print(level)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Rune类
# class Rune(object):
#     # Todo:初始化属性name, color, attribute, attributeValue, level
#     def __init__(self, name, color, attribute, attributeValue, level):
#         self.name = name
#         self.color = color
#         self.attribute = attribute
#         self.attributeValue = attributeValue
#         self.level = level
#         # Todo:在Rune类中打印输出属性的值
#         print("Rune:%s,%s,%s,%d,%d" % (self.name, self.color, self.attribute, self.attributeValue, self.level))
#
#
# # Todo: 输入五行字符，按照顺序依次为Rune类对象的名称(name)、颜色(color)、属性名称(attribute)、属性值(attributeValue)、等级(level)初始化
# name = '地狱'
# color = '蓝色'
# attribute = '攻击力'
# attributeValue = 50
# level = 1
#
# # Todo:实例化Rune对象,打印输出结果
# Rune(name, color, attribute, attributeValue, level)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # Todo:补全Rune类
# class Rune(object):
#     # Todo:初始化属性name, color, attribute, attributeValue, level
#     def __init__(self, name, color, attribute, attributeValue, level):
#         self.name = name
#         self.color = color
#         self.attribute = attribute
#         self.attributeValue = attributeValue
#         self.level = level
#
#     # Todo:  传入参数为：铭文数量，没有返回值。
#     #       最初级的铭文为1级，5个1级铭文可以合成1个2级铭文，5个2级铭文可以合成3级铭文，以此类推.......
#     #       铭文每提升一个等级，属性值增加20%。
#     def levelUp(self, number):
#         for i in range(10):
#             if 5 ** (i - 1) < number <= 5 ** i:
#                 self.level = i
#                 for i in range(self.level-1):
#                     self.attributeValue += self.attributeValue * 0.2
#                 continue
#
#     # 打印输出对象信息
#     def printObj(self):
#         self.attributeValue = round(self.attributeValue)
#         print('Rune:{0},{1},{2},{3},{4}'.format(self.name, self.color, self.attribute, self.attributeValue, self.level))
#
#
# # Todo: 输入五行字符，按照顺序依次为Rune类对象的名称(name)、颜色(color)、属性名称(attribute)、属性值(attributeValue)、等级(level)初始化
# name = '地狱'
# color = '蓝色'
# attribute = '攻击力'
# attributeValue = 50
# level = 1
#
# # Todo:实例化Rune对象
# r = Rune(name, color, attribute, attributeValue, level)
#
# # Todo:调用levelUp方法，实现铭文提升等级的功能
# r.levelUp(15)
#
# # Todo:调用printObj方法，打印输出对象信息
# r.printObj()


# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 初始化颜色等级限制的字典
# 白色-3，绿色-5，蓝色-7，橙色-9，红色-12。
dictLevel = {'白色': 3, '绿色': 5, '蓝色': 7, '橙色': 9, '红色': 12}


# Todo:补全Rune类
class Rune(object):
    # Todo:初始化属性name, color, attribute, attributeValue, level
    def __init__(self, name, color, attribute, attributeValue, level):
        self.name = name
        self.color = color
        self.attribute = attribute
        self.attributeValue = attributeValue
        self.level = level

    # Todo:  传入参数为：铭文数量，没有返回值。
    #       铭文每提升一个等级，属性值增加20%。
    #       铭文根据不同的颜色，提升等级的上限不同，白色-3，绿色-5，蓝色-7，橙色-9，红色-12。
    #       达到等级上限，铭文等级不可提升
    def levelUp(self, number):
        data = {'白色': 3, '绿色': 5, '蓝色': 7, '橙色': 9, '红色': 12}
        for i in range(data[self.color] + 1):
            if 5 ** (i - 1) <= number <= 5 ** i:
                self.level = i
                for i in range(self.level - 1):
                    self.attributeValue += self.attributeValue * 0.2
                continue
            elif number > 5 ** data[self.color]:
                self.level = data[self.color]
                for i in range(self.level - 1):
                    self.attributeValue += self.attributeValue * 0.2
                continue

    # 打印输出对象信息
    def printObj(self):
        self.attributeValue = round(self.attributeValue)
        print('Rune:{0},{1},{2},{3},{4}'.format(self.name, self.color, self.attribute, self.attributeValue, self.level))


# Todo: 输入五行字符，按照顺序依次为Rune类对象的名称(name)、颜色(color)、属性名称(attribute)、属性值(attributeValue)、等级(level)初始化
name = '地狱'
color = '蓝色'
attribute = '攻击力'
attributeValue = 50
level = 1

# Todo:实例化Rune对象
r = Rune(name, color, attribute, attributeValue, level)

# Todo:调用levelUp方法，实现铭文提升等级的功能
r.levelUp(15)

# Todo:调用printObj方法，打印输出对象信息
r.printObj()