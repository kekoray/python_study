# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 17:35
# @Author : koray
# @File :

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 共有五个主题：暗网格(darkgrid)，白网格(whitegrid)，全黑(dark)，全白(white)，全刻度(ticks)
# 在 seaborn 中设置主题使用 set_style（）方法
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
plt.plot(x, c, color="blue", linewidth=1.0, label="blue", linestyle="--")
plt.plot(x, s, color="green", linewidth=1.0, label="Green", linestyle="-.")
plt.legend()  # 显示设置的图例
plt.xlim(-4.0, 4.0)  # 设置 x 轴范围
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))  # 设置 x 轴刻度
plt.ylim(-1.0, 1.0)  # 设置 y 轴范围
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))  # 设置 y 轴刻度
# plt.savefig("exercice.png", dpi=80)  # 保存图像，分辨率为 80
plt.show()

plt.figure(dpi=80)
plt.plot(x, c, color="red", linewidth=4.0, label="blue", linestyle="--")
plt.plot(x, s, color="blue", linewidth=0.5, linestyle="-", marker="1")
plt.show()
