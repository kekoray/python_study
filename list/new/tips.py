# -*- coding: utf-8 -*- 
# @Time : 2021/8/9 16:54
# @Author : koray
# @File :


""" 小技巧 """

''' =========== 1.变量值互换与多元赋值 ==================== '''
a = 3
b = 2
a, b = b, a
c, d = 8, 9

''' =========== 2.三元表达式(true if 条件 else false),比较2个数字的大小 ==================== '''
a = 8
b = 9
print(a if a > b else b)

''' =========== 3.推导式生成数据 ==================== '''
# 列表
List = [i ** 2 for i in range(-5, 5) if i % 2]  # [25, 9, 1, 1, 9]
# 集合
Set = {i ** 2 for i in range(-5, 5) if i % 2}  # {25, 9, 1}
# 字典
Dict = {x: y for x, y in zip(["a", "b"], (1, 2))}  # {'a': 1, 'b': 2}

''' =========== 4.小整数对象池 ==================== '''
# python为了优化速度,使用[-5,256]范围的小整数对象池,避免了整数频繁申请和销毁内存空间,这些整数对象会提前建立好,不会被回收.
a = 0
b = 0
print(id(a) == id(b))  # True

# 当字符串中不存在空格和特殊字符时,也有一样的优化
i = "kk"
l = "kk"
print(i is l)  # True

''' =========== 5.数据解包 ==================== '''
# 数据解包
# 需求:获取一个列表中的数据
# 1.for循环
for i in [1, 2, 3]:
    print(i)
# 2.使用相同数量的变量接收
a, b, c = [1, 2, 3]
# 3.使用星号*解包
L = [1, 3, 3]
print(*L)  # 1 3 3
