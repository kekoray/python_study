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

# 创建多维形状的未初始化数组, np.empty(shape, dtype=float, order='C')  todo: ???
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

# 数组的维度 (行数,列数)
print(a.shape)  # (3, 2)
# 数组元素的个数
print(a.size)  # 6

# 数组第一维度上的大小,即行数;数组第二维度上的大小,即列数;
print(a.shape[0])  # 行数  ==>  3
print(a.shape[1])  # 列数  ==>  2
print(np.size(a, 0))  # 行数  ==>  3
print(np.size(a, 1))  # 列数  ==>  2
print(len(a))  # 行数  ==>  3

# 获取数组的维度数
print(a.ndim)  # 2维数据
b = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]])
print(b.ndim)  # 3维数据

# 数组常用操作

# 获取值
a = np.arange(10)  # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a[1]  # 1
a[0:3]  # array([0, 1, 2])
# slice类似设定切片规则传入
s = slice(0, 3)
a[s]  # array([0, 1, 2])

#  ========================  数据的切片与索引
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
'''
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
'''
# 数组索引操作  todo :  === 有问题,不知道
a[2]  # array([6, 7, 8])
a[[0, 1], [0, 0]]

# 数组切片操作: 数组[行操作,列操作],下标包头不包尾
a[:2, :3]  # array([[0, 1, 2], [3, 4, 5]])
a[2, :]  # array([6, 7, 8])
a[2:, :]  # array([[6, 7, 8]])

# 布尔运算获取值,判断每个元素是否符合条件
a[a > 4]  # array([5, 6, 7, 8])

# 改变数组维度,但是不能改变数组元素个数
a.reshape(1, 9)  # array([[0, 1, 2, 3, 4, 5, 6, 7, 8]])

'''  ================================  数组广播
广播(Boardcasting)是NumPy中用于在不同大小的阵列之间进行逐元素运算的一组规则
'''

"""两个array的shape长度与shape的每个对应值都相等的时候，那么结果就是对应元素逐元素运算，运算的结果 shape 不变"""
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
print(a * b)  # array([ 1,  4,  9, 16])
print(a + 5)  # array([6, 7, 8, 9])

"""shape长度不相等时,先把短的shape前面一直补1，直到与长的shape长度相等时，
此时两个array的shape对应位置上的值：1.相等  2.其中一个为1，这样才能进行广播。
"""
a = np.arange(9).reshape([3, 3])
b = np.array([1, 2, 3])
print(a + b)
'''
array([[0, 1, 2],      array([[1, 2, 3]])           array([[ 1,  3,  5],
       [3, 4, 5],   +  array([[1, 2, 3]])   ====>          [ 4,  6,  8],
       [6, 7, 8]])     array([[1, 2, 3]])                  [ 7,  9, 11]])
'''

''' =========================== 常用函数 '''

''' =========================== 矩阵创建 '''

# 创建矩阵
import numpy.matlib

# 全零矩阵
np.matlib.zeros([2, 2])
# 全一矩阵
np.matlib.ones([2, 2])
# 对角矩阵
np.matlib.eye(3)
# 随机生成矩阵
np.matlib.rand(2, 2)  # matrix([[0.15843201, 0.84915475],  [0.8656387 , 0.51666915]])
# 调用mat/matrix/asmatrix函数,将数据转化为矩阵   todo: 补充...
a = np.array([[1, 2], [3, 4]])
b = np.mat(a)  # matrix([[1, 2], [3, 4]])
d = np.asmatrix(a)  # masmatrix 处理矩阵或数组时不复制
c = np.matrix(a)  # 类似 array 和 asarray

''' =========================== 矩阵运算 '''
a = np.mat([[1], [2], [3]])
b = np.mat([1, 2, 3])
print(a * b)
'''
matrix([[1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]])
'''

# 对应元素相乘
a = np.mat([1, 2, 3])
a * 2  # matrix([[2, 4, 6]])
b = a
c = np.multiply(a, b)
print(c)  # matrix([[1, 4, 9]])

# 矩阵求逆
a = np.matrix([[2, 0, 0], [0, 1, 0], [0, 0, 2]])
b = a.I
print(b)
'''
matrix([[0.5, 0. , 0. ],
        [0. , 1. , 0. ],
        [0. , 0. , 0.5]])
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
