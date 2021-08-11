# -*- coding: utf-8 -*-
# @Time : 2021/8/10 10:37
# @Author : koray
# @File :

import numpy as np


class a(object):
    pass


'''================ 数组创建 ======================='''
# 创建数组
np.array([2, 5, 7])  # 一维数组 ==> array([2 5 7])
np.array([[2, 5, 7], [8, 9, 0]])  # 多维数组 ==> array([[2, 5, 7], [8, 9, 0]])

# 将数据转化为数组, np.asarray(a, dtype = None, order = None)
a = [1, 2, 3, 4]
np.asarray(a)  # array([1, 2, 3, 4])

# 创建多维形状的未初始化数组,打印的值是随机无意义的, np.empty(shape, dtype=float, order='C')
np.empty([2, 2])

# 生成类似于对角矩阵的数组  [N为行数,M为列数,k为对角线的索引,0代表主对角线]
# np.eye(N, M=None, k=0, dtype=float, order='C')

np.eye(4, 4, 0)
'''
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
'''

# 创建多维形状的全零数组, np.zeros(shape, dtype=float, order='C')
np.zeros([2, 2])  # array([[0., 0.], [0., 0.]])

# 创建多维形状的全1数组, np.ones(shape, dtype=None, order='C')
np.ones([2, 2])  # array([[1., 1.], [1., 1.]])

# 创建多维形状的全指定原元素值的数组
np.full([2, 2], 8)  # array([[8., 8.], [8., 8.]])

# 生成等间隔的数组, np.arange(start, stop, step, dtype)
np.arange(0, 10, 2)  # array([0 2 4 6 8])

# 生成等间隔的数组,
np.linspace(1, 2,
            num=10)  # array([1. 1.11111111 1.22222222 1.33333333 1.44444444 1.55555556 1.66666667 1.77777778 1.88888889 2.  ])

'''================ 数组操作 ======================='''

# 获取数组属性
a = np.array([[1, 2], [3, 4], [5, 6]])
'''
array([[1, 2],
       [3, 4],
       [5, 6]])
'''

# 数组的形状维度 (行数,列数)
print(a.shape)  # (3, 2)
# 获取数组的维度数
print(a.ndim)  # 2维数据
b = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]])
print(b.ndim)  # 3维数据
# 数组元素的个数
print(a.size)  # 6
# 改变数组维度,但是不能改变数组元素个数
print(a.reshape(2, 3))  # array([[1, 2, 3], [4, 5, 6]])

# 数组第一维度上的大小,即行数;数组第二维度上的大小,即列数;
print(a.shape[0])  # 行数  ==>  3
print(a.shape[1])  # 列数  ==>  2
print(np.size(a, 0))  # 行数  ==>  3
print(np.size(a, 1))  # 列数  ==>  2
print(len(a))  # 行数  ==>  3

#  ========================  数组的切片与索引操作
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

# 索引操作
a[2]  # array([6, 7, 8])
# a[[第1个值的行下标,第2个值的行下标], [第1个值的列下标,第2个值的列下标]]
a[[2, 0], [0, 2]]  # array([6, 2])

# 切片操作: 数组[行操作,列操作],下标包头不包尾
a[:2, :3]  # array([[0, 1, 2], [3, 4, 5]])
a[2, :]  # array([6, 7, 8])
a[2:, :]  # array([[6, 7, 8]])
# slice类似设定切片规则传入
s = slice(0, 3)
a[s]  # array([0, 1, 2])

# 布尔运算获取值,判断每个元素是否符合条件
a[a > 4]  # array([5, 6, 7, 8])

'''  ================================  数组广播
广播(Boardcasting)是NumPy中用于在不同大小的阵列之间进行逐元素运算的一组规则,
对于不同形状的数组,对较小的数组进行拓展,与较大数组进行匹配运算.
'''

'''两个数组的shape长度相等时,对应元素逐元素运算'''
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
print(a * b)  # array([ 1,  4,  9, 16])
print(a + 5)  # array([6, 7, 8, 9])

'''两个数组的shape长度不相等时,对应元素逐元素运算,对较小数组进行自身拓展,再与较大数组进行逐元素运算'''
a = np.arange(9).reshape([3, 3])
b = np.array([1, 2, 3])
print(a + b)
'''
array([[0, 1, 2],      array([[1, 2, 3]])           array([[ 1,  3,  5],
       [3, 4, 5],   +  array([[1, 2, 3]])   ====>          [ 4,  6,  8],
       [6, 7, 8]])     array([[1, 2, 3]])                  [ 7,  9, 11]])
'''

''' =========================== 常用函数 
ufunc是universal function缩写,是一种能对数组的每个元素进行操作的函数
'''

# 算术函数
# 基本
np.add()
np.multiply()
np.negative()
np.divide()
np.remainder()

# 三角
np.sin()
np.cos()
np.tan()
# 舍入
np.around()
np.floor()
np.ceil()
# 余数
np.mod()
# 平方,乘方,平方根
np.square()
np.power()
np.sqrt()

# 统计相关
np.sum()
np.mean()
np.std()
np.var()
np.max()
np.min()
np.ptp()
np.sort()
np.argsort()
np.unique()
np.bincount()

# 解线性方程组
np.linalg()
np.inv()
np.solve()

# ================

# 对数组进行维度转换             todo:????
a = np.arange(12).reshape(2, 2, 3)
b = np.transpose(a, (2, 0, 1))

# 根据指定维度(行,列)方向进行拼接
# 默认为axis=0,即根据第1维度的行进行拼接,当axis=1,即根据第2维度的列进行拼接
a = np.arange(6).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
np.concatenate((a, b))  # 维度(4,3) ==> array([[ 0,  1,  2], [ 3,  4,  5], [ 7,  8,  9], [10, 11, 12]])
np.concatenate((a, b), axis=1)  # 维度(2,6) ==> array([[ 0,  1,  2,  7,  8,  9],  [ 3,  4,  5, 10, 11, 12]])

# 根据指定维度(行,列)方向进行堆叠数组,与concatenate不同的是会拓展维度
# 当axis=0,即根据第1维度的行进行堆叠,当axis=1,即根据第2维度的列进行堆叠
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
np.stack((a, b), 0)  # array([[[1, 2], [5, 6]], [[3, 4], [7, 8]]])
np.stack((a, b), 1)  # array([[[1, 2], [5, 6]], [[3, 4], [7, 8]]])

# 根据指定维度(行,列)方向,在数组的后面追加values,values的维度要与数组的指定维度数一致
# 当axis=0,即根据第1维度的行进行追加,当axis=1,即根据第2维度的列进行追加
a = np.arange(6).reshape(2, 3)
np.append(a, [[7, 8, 9]], axis=0)  # array([[0, 1, 2], [3, 4, 5]])
np.append(a, [[7, 8, 9], [10, 11, 12]], axis=1)  # array([[ 0,  1,  2,  7,  8,  9], [ 3,  4,  5, 10, 11, 12]])

# 根据指定维度(行,列)方向,在数组的指定索引位置插入values,values的维度要与数组的指定维度数一致
# 当axis=0,即根据第1维度的行进行插入,当axis=1,即根据第2维度的列进行插入
a = np.arange(6).reshape(2, 3)
np.insert(a, 1, [[7, 8, 3], [9, 10, 3]], axis=0)  # array([[ 0,  1,  2], [ 7,  8,  3], [ 9, 10,  3], [ 3,  4,  5]])
np.insert(a, 2, [7, 8], axis=1)  # array([[0, 1, 7, 2], [3, 4, 8, 5]])

# 根据指定维度(行,列)方向,在数组的指定索引位置进行删除操作
# 当axis=0,即根据第1维度的行进行删除,当axis=1,即根据第2维度的列进行删除
a = np.arange(6).reshape(2, 3)
np.delete(a, 0, axis=0)  # array([[3, 4, 5]])
np.delete(a, 1, axis=1)  # array([[0, 2], [3, 5]])

''' =========================== 矩阵创建 '''

# 导包
import numpy.matlib

# 创建矩阵
b = np.mat([[1, 2], [3, 4]])  # matrix([[1, 2], [3, 4]])
c = np.matrix([[1, 2], [3, 4]])  # matrix([[1, 2], [3, 4]])
d = np.asmatrix([[1, 2], [3, 4]])  # matrix([[1, 2], [3, 4]])
# 全零矩阵
np.matlib.zeros([2, 2])  # matrix([[0., 0.], [0., 0.]])
# 全一矩阵
np.matlib.ones([2, 2])  # matrix([[1., 1.], [1., 1.]])
# 对角矩阵
np.matlib.eye(3)  # matrix([[1., 0.], [0., 1.]])
# 随机生成矩阵
np.matlib.rand(2, 2)  # matrix([[0.15843201, 0.84915475],  [0.8656387 , 0.51666915]])

"""
Numpy数组和矩阵的区别:
matrices必须是2维的,arrays可以是多维
matrix是array的分支,拥有array的所有特性

如果两个可以通用，那就选择array，因为array更灵活，速度更快;
arrays可以使用简单运算做元素相乘,而矩阵相乘,则需要numpy里面的dot命令

运算符的作用也不一样 ：因为a是个matrix，所以a**2返回的是a*a，相当于矩阵相乘。而c是array，c**2相当于，c中的元素逐个求平方
两条命令轻松的实现两者之间的转换：np.asmatrix和np.asarray
numpy 中的array与numpy中的matrix的最大的不同是，在做归约运算时，array的维数会发生变化，但matrix总是保持为2维
"""

''' =========================== 矩阵运算 '''
a = np.mat([[1], [2], [3]])
b = np.mat([1, 2, 3])
print(a * b)  # matrix([[1, 2, 3], [2, 4, 6], [3, 6, 9]])

# 对应元素相乘
a = np.mat([1, 2, 3])
a * 2  # matrix([[2, 4, 6]])
b = a
c = np.multiply(a, b)
print(c)  # matrix([[1, 4, 9]])

# 矩阵求逆
a = np.matrix([[2, 0, 0], [0, 1, 0], [0, 0, 2]])
print(a.I)
'''
matrix([[0.5, 0. , 0. ],
        [0. , 1. , 0. ],
        [0. , 0. , 0.5]])
'''
# 矩阵转置
print(a.T)
'''
matrix([[2, 0, 0],
        [0, 1, 0],
        [0, 0, 2]])
'''

# 行列式计算   todo :  ?????
a = np.matrix([[1, 2], [3, 4]])
b = np.linalg.det(a)
print(b)  # -2.0000000000000004

# 求和与最大最小
a = np.matrix([[1, 2], [3, 4]])
print(a.sum(axis=0))  # 列求和  ==>  matrix([[4, 6]])
print(a.sum(axis=1))  # 行求和  ==>  matrix([[3], [7]])
print(a.max())  # 4
print(a.min())  # 1

# 矩阵转数组,getA()将矩阵类转化为数组类
a = np.mat([[1, 2, 3], [4, 5, 6]])
b = a.getA()
print(b)  # array([[1, 2, 3], [4, 5, 6]])
