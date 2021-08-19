# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 17:35
# @Author : koray
# @File :

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 共有五个主题：暗网格(darkgrid)，白网格(whitegrid)，全黑(dark)，全白(white)，全刻度(ticks)
plt.style.use("seaborn-ticks")  # 选择图形主题（默认为全刻度）
x = np.arange(0, 3 * np.pi, 0.1)  # 生成数组 x
# numpy.sin(x[, out])：生成 x 中数据的正弦值数组
y = np.sin(x)  # 对于 x 中的每个元素取正弦值
# matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)：绘制曲线图。*args 中包括了所需要的数据，曲线的颜色和样式等。
plt.plot(x, y)  # 根据传入的数据，绘制曲线图
plt.show()  # 显示图形

''' ============= 绘制子图 ========='''
plt.style.use("seaborn-whitegrid")
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

'''
# 在当前画布中添加子图,*args是三个独立的整数(画布行数,画布列数,选中号),用于描述子图的位置
matplotlib.pyplot.subplot（*args，**kwargs）
'''
# 将画布分为2行1列两个子图,选中第一个子图做数据配置
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()

''' ============= 图形参数 =========
以调整 matplotlib 图像中的各个参数（x，y 轴、图例、颜色……）
'''
plt.style.use("seaborn-dark")
# 创建一个8x6大小的图像,dpi=80表示分辨率每英尺80点
plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(111)  # 等价于(1,1,1)
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)
plt.plot(x, c, color="blue", linewidth=1.0, label="Blue", linestyle="--")
plt.plot(x, s, color="green", linewidth=1.0, label="Green", linestyle="-.")
plt.legend()  # 显示设置的图例
plt.xlim(-4.0, 4.0)  # 设置 x 轴范围
plt.ylim(-1.0, 1.0)  # 设置 y 轴范围
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))  # 设置 x 轴刻度
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))  # 设置 y 轴刻度
# plt.savefig("exercice.png", dpi=80)  # 保存图像，分辨率为 80
plt.show()

plt.figure(dpi=80)
plt.plot(x, c, color="red", linewidth=4.0, linestyle="--")
plt.plot(x, s, color="blue", linewidth=0.5, linestyle="-", marker="x")
plt.show()

''' ============= 散点图 ========='''
a = np.random.randint(0, 20, 15)
b = np.random.randint(0, 20, 15)
# 绘制散点图
plt.scatter(a, b)
plt.show()

''' ============= 柱状图 ========='''
from pylab import mpl

# 解决中文不显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']
level = ['优秀', '不错', '666']
x = range(len(level))
y = [1, 3, 2]
plt.figure(dpi=100)
plt.bar(x, y, width=0.5, color=['b', 'r', 'g'])
plt.xticks(x, level)
# 添加网格显示
plt.grid(linestyle="--", alpha=0.5)
plt.show()

''' ============= 直方图  ========='''
t = np.random.randint(0, 30, 90)
plt.figure(dpi=100)
distance = 2  # 设置组距
group_num = int((max(t) - min(t)) / distance)  # 计算组数
plt.hist(t, facecolor="blue", edgecolor="black", alpha=0.7)
plt.xticks(range(min(t), max(t))[::2])
# 添加网格显示
plt.grid(linestyle="--", alpha=2)
plt.show()

''' ============= 绘画步骤  ========='''

# 导包
# 3D
from mpl_toolkits.mplot3d import Axes3D

# 创建3D画布
fig = plt.figure()
ax = Axes3D(fig)

# 曲面图
ax.plot_surface(x, y, z)
# 散点图
ax.scatter(x, y, z)
ax.plot()
ax.bar3d()

# 设置z轴的范围
ax.set_zlim3d()
# 设置z轴的标签
ax.set_zlabel()

# 1.创建画布
plt.figure(figsize=None,
           dpi=None,
           facecolor=None,
           edgecolor=None,
           frameon=True,
           clear=False, )
'''
1.设置画布大小
2.设置背景颜色
3.设置边框
4.设置分辨率
'''

# 2.选择图形,填充数据
'''
2D图表函数
折线图:plot()
直方图:bar()
饼图:pie()
'''
plt.plot()
plt.bar()
plt.pie()

# 3.设置图形细节
'''
设置刻度,轴标签
标题
图例
说明文档
使用主题
数据标记-数据点样式
网格
线条
颜色
'''
# 网格
plt.grid(b=True, axis=['both' | 'x' | 'y'])
# 图例
plt.legend(loc=2, fontsize=2, frameon='', title='')

# 4.保存并展示
plt.savefig("/保存路径.jpg")
plt.show()
