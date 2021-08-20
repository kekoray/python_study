# -*- coding: utf-8 -*- 
# @Time : 2021/8/20 17:56
# @Author : koray
# @File :

import numpy as np
import pandas as pd

'''创建series'''

# 1.直接创建
pd.Series([1, 2, 3, np.nan, 9, 0])

# 2.数组创建,默认带索引
pd.Series(np.array(['a', 'b', 'c']))

# 3.字典创建,索引为字典的键
pd.Series({'a': 1, 'b': 2, 'c': 3})

'''创建DataFrame
DataFrame 既有行索引，也有列索引，可以看做是 Series 组成的字典，每个 Series 看做 DataFrame的一个列
'''

# 通过字典创建DataFrame
pd.DataFrame({'A': 1.,
              'B': pd.Timestamp('2021-01-01'),  # Timestamp 方法生成时间戳
              'C': pd.Series(1, list(range(4)), dtype='float32'),
              'D': np.array([3] * 4),
              #  Categoricals 是 pandas 的一种数据类型，对应着被统计的变量,具有特定的顺序，这个顺序是创建时手工设定的，是静态的
              'E': pd.Categorical(["test", "train", "test", "train"]),
              'F': 'foo'})

# 通过时间序列创建DataFrame
# 生成作为行索引的时间序列
'''
时间序列生成：pandas.date_range（start = None，end = None，periods = None，freq =
"D"，tz = None，normalize = False，name = None，closed = None，**kwargs ）：生成一个时
间序列的索引 DatetimeIndex。start 为日期起点，end 为日期终点，periods 为个数，freq 表示间隔
（D 表示以日为间隔）,tz 表示时区
'''
dates = pd.date_range("2021-01-01", periods=7)
pd.DataFrame(np.random.randn(7, 5), index=dates, columns=list("ABCDE"))
