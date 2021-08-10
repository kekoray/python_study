# -*- coding: utf-8 -*- 
# @Time : 2021/8/10 10:37
# @Author : koray
# @File :

import numpy as np

'''================ 数组创建 ======================='''
# 创建数组
np.array([2, 5, 7])  # 一维数组 ==> array([2 5 7])
np.array([[2, 5, 7], [8, 9, 0]])  # 多维数组 ==> array([[2, 5, 7], [8, 9, 0]])

# 将数据转化为数组, np.asarray(a, dtype = None, order = None)
a = [1, 2, 3, 4]
np.asarray(a)  # array([1, 2, 3, 4])

# 创建矩阵的未初始化数组, np.empty(shape, dtype=float, order='C')
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

# 创建矩阵的全零数组, np.zeros(shape, dtype=float, order='C')
np.zeros([2, 2])  # array([[0., 0.], [0., 0.]])

# 创建矩阵的全1数组, np.ones(shape, dtype=None, order='C')
np.ones([2, 2])  # array([[1., 1.], [1., 1.]])

# 生成等间隔的数组, np.arange(start, stop, step, dtype)
np.arange(0, 10, 2)  # array([0 2 4 6 8])

# 生成等间隔的数组,
np.linspace(1, 2, num=10)
'''
array([1.         1.11111111 1.22222222 1.33333333 1.44444444 1.55555556
       1.66666667 1.77777778 1.88888889 2.        ])
'''

# 获取数组属性
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.shape)        # (3, 2)
print(a.shape[1])     # 3
print(a.size)         # 6
print(np.size(a, 0))  # 3
print(len(a))         # 3

#
# a = np.arange(10)  # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# a[1]  # 1
# a[0:3]  # array([0, 1, 2])
#
# # 类似切片参数设定
# s = slice(0, 3)
# a[s]  # array([0, 1, 2])
#
# # 数据的切片与索引
#
# a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# #  [[0 1 2]
# #   [3 4 5]
# #   [6 7 8]]
#
# a[:2, :3]  # array([[0, 1, 2], [3, 4, 5]])
# a[2]  # array([6, 7, 8])
# a[2, :]  # array([6, 7, 8])
# a[2:, :]  # array([[6, 7, 8]])
#
# # 通过布尔运算得结果
# a[a > 6]  # array([7, 8])
#
# # 数组的广播
# # 广播是指...  多维数组的运算
#
# a = np.array([[1, 2], [3, 4]])
# b = np.array([1, 2])
#
# # print(a+b )
# # [[2 4]
# #  [4 6]]
#
# print(a + 5)
# # [[6 7]
# #  [8 9]]
#
#
# # 数组常用操作
#
# np.reshape(a, newshape)
#
# # ufunc运算
#
# # random模块
# np.random.rand()
# np.randomr.randn()
# np.random.randint()
