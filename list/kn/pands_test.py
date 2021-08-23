# -*- coding: utf-8 -*- 
# @Time : 2021/8/20 17:56
# @Author : koray
# @File :

import numpy as np
import pandas as pd

#
# '''创建series'''
#
# # 1.直接创建
# pd.Series([1, 2, 3, np.nan, 9, 0])
#
# # 2.数组创建,默认带索引
# pd.Series(np.array(['a', 'b', 'c']))
#
# # 3.字典创建,若不指定索引,则索引为字典的键
# pd.Series({'a': 1, 'b': 2, 'c': 3})
#
# # 通过Series的values和index属性获取其数组表示形式和索引对象
# s = pd.Series(np.array(['a', 'b', 'c']))
# s.values  # array(['a', 'b', 'c'], dtype=object)
# s.index  # RangeIndex(start=0, stop=3, step=1)
#
# '''创建DataFrame
# DataFrame是一个表格型的数据结构, 它含有一组有序的列, 每列可以是不同的值类型
# DataFrame既有行索引,也有列索引,可以看做是Series组成的字典,每个Series看做DataFrame的一个列
# '''
#
# # 1.通过字典创建DataFrame
# pd.DataFrame({'A': 1.,
#               'B': pd.Timestamp('2021-01-01'),  # Timestamp 方法生成时间戳
#               'C': pd.Series(1, list(range(4)), dtype='float32'),
#               'D': np.array([3] * 4),
#               #  Categoricals 是 pandas 的一种数据类型, 对应着被统计的变量,具有特定的顺序, 这个顺序是创建时手工设定的, 是静态的
#               'E': pd.Categorical(["test", "train", "test", "train"]),
#               'F': 'foo'})
#
# # 2.通过时间序列创建DataFrame
# '''
# 时间序列生成：pandas.date_range（start = None, end = None, periods = None, freq =
# "D", tz = None, normalize = False, name = None, closed = None, **kwargs ）：生成一个时
# 间序列的索引 DatetimeIndex. start 为日期起点, end 为日期终点, periods 为个数, freq 表示间隔
# （D 表示以日为间隔）,tz 表示时区
# '''
# # 生成作为行索引的时间序列
# dates = pd.date_range(start="2021-01-01", end="2021-02-01", periods=7)
# # 指定时间序列为索引
# pd.DataFrame(np.random.randn(7, 5), index=dates, columns=list("ABCDE"))
# '''
#
#                         A	        B	        C	        D	        E
# 2021-01-01 00:00:00	0.750120	-0.094547	-0.459937	0.767405	-1.748746
# 2021-01-06 04:00:00	-2.362144	-0.702300	0.476891	0.031054	-0.021801
# 2021-01-11 08:00:00	0.764357	0.662128	0.340510	-0.194788	-0.826951
# 2021-01-16 12:00:00	0.378670	0.437846	0.671887	1.355264	-0.896017
# 2021-01-21 16:00:00	-0.357642	-0.053722	0.958072	-0.288953	1.743930
# 2021-01-26 20:00:00	-0.279510	0.251506	0.496458	-2.000370	0.576176
# 2021-02-01 00:00:00	1.659798	1.079884	0.255388	-0.142203	1.559521
# '''
#
# '''常用操作'''
#
# data = np.arange(15).reshape([3, 5])
# df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D', 'E'])
# print(df)
# '''
#     A   B   C   D   E
# a   0   1   2   3   4
# b   5   6   7   8   9
# c  10  11  12  13  14
# '''
# # 显示前n条数据
# print(df.head(2))
# '''
#    A  B  C  D  E
# a  0  1  2  3  4
# b  5  6  7  8  9
# '''
# # 显示底部的n条数据
# print(df.tail(1))
# '''
#     A   B   C   D   E
# c  10  11  12  13  14
# '''
# # 获取索引
# print(df.index)  # Index(['a', 'b', 'c'], dtype='object')
#
# # 修改索引
# df.index = [1, 2, 3]
#
# # 获取列
# print(df.columns)  # Index(['A', 'B', 'C', 'D', 'E'], dtype='object')
#
# # 修改列名
# df.columns = ['A2', 'B2', 'C2', 'D2', 'E2']
#
# #  获取数据
# print(df.values)  # array([[ 0,  1,  2,  3,  4],[ 5,  6,  7,  8,  9],[10, 11, 12, 13, 14]])
#
# # 根据列名对相关索引进行切片操作
# print(df.loc['a':'c':2, 'A'])
# '''
# 获取A列,索引为a到c(包括c)中的数据,步长为2
# a     0
# c    10
# Name: A, dtype: int32
# '''
#
# # 查看数据的详细信息
# print(df.describe())
# '''
#            A     B     C     D     E
# count   3.0   3.0   3.0   3.0   3.0       # 一列的元素个数
# mean    5.0   6.0   7.0   8.0   9.0       # 一列数据的平均值
# std     5.0   5.0   5.0   5.0   5.0       # 一列数据的均方差,反映一个数据集的离散程度
# min     0.0   1.0   2.0   3.0   4.0       # 一列数据中的最小值
# 25%     2.5   3.5   4.5   5.5   6.5       # 一列数中的最大值
# 50%     5.0   6.0   7.0   8.0   9.0       # 一列数据中, 前 25% 的数据的平均值
# 75%     7.5   8.5   9.5  10.5  11.5       # 一列数据中, 前 50% 的数据的平均值
# max    10.0  11.0  12.0  13.0  14.0       # 一列数据中, 前 75% 的数据的平均值
#
# '''
#
# """ ============= 数据操作"""
# # 使用drop方法删除不需要的列或行
# a = df.drop(['a'], axis=0)
# b = df.drop(['A'], axis=1)
#
# # 使用append方法合并两个DataFrame
# c = a.append(b)
# print(c)
# '''
#       A   B   C   D   E
# b   5.0   6   7   8   9
# c  10.0  11  12  13  14
# a   NaN   1   2   3   4
# b   NaN   6   7   8   9
# c   NaN  11  12  13  14
# '''
#
# # 使用reset_index方法还原索引, 让索引变为数据中的一列  todo:?????
# df.reset_index(inplace=True)  # inplace为true时会修改原始数据,为False会产生新的数据
#
# # 使用iteritems方法遍历每列数据,返回一个包含列名称和列内容为系列的元组
# n = 1
# for s in df.iteritems():
#     print("第%d列数据%s" % (n, s))
#     n += 1
# '''
# 第1列数据('A', a     0
# b     5
# c    10
# Name: A, dtype: int32)
# 第2列数据('B', a     1
# b     6
# c    11
# Name: B, dtype: int32)
#         ...
# '''
#
# print("===" * 20)
#
# """================  Pandas统计函数  """
# # ====================  计算当前元素和先前元素之间的百分比变化  =======================
# '''
#  pct_change()函数, 函数将每个元素与其前一个元素进行比较, 并计算百分比变化.
#  DataFrame.pct_change（periods= 1, fill_method ='pad', limit = None, freq = None, ** kwargs ）
#  periods为形成百分比变化的时期, fill_method为如何在计算百分比变化之前处理NA, limit表示停止前要填充的连续NA的数量
# '''
# s = pd.Series([1, 2, 3, 4, 5, 4, 2])
# print(s.pct_change())
#
# # ====================  计算协方差  =======================
# '''
#  Series.cov（min_periods = None）
#  计算列的协方差,不包括NA/null值, min_periods表示每个列对所需的最小观测值数
# '''
# s1 = pd.Series(np.random.randn(10))
# s2 = pd.Series(np.random.randn(10))
# print(s1.cov(s2))
#
# # 当应用于DataFrame时,则需要计算所有列之间的协方差(cov)值.
# df = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
# print(df.cov())
#
# # ====================  根据每行数据的大小返回名次  =======================
# '''
#  DataFrame.rank（axis = 0,method ='average',numeric_only = None,na_option ='keep',ascending = True,pct = False ）
#  axis选择行或列,method ='average'表示对平均值排名（可以取一下几个值'average','min','max','first','dense'）,
#  ascending = True表示降序排序,na_option ='keep'表示将NA值保留在原来的位置
# '''
# s3 = pd.Series(np.random.randn(5), index=list('abcde'))
# s3.rank()
# '''
# a    4.0
# b    1.5
# c    5.0
# d    1.5
# e    3.0
# dtype: float64
# '''
# # ====================  分组聚合统计  =======================
# # 根据c列进行分组,计算a列的总分和平均分
# df = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
# df.groupby('c')['a'].agg([np.sum, np.mean])
#
# """ ========= ==  缺失数据的简单操作"""
#
# # 示例
# df2 = pd.DataFrame(np.random.rand(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
#
# # 使用reindex方法设置新的索引,多出的索引对应数据使用NaN填充
# df3 = df2.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# '''
#         one       two     three
# a  0.505405  0.476354  0.232798
# b       NaN       NaN       NaN
# c  0.945555  0.684889  0.989451
# d       NaN       NaN       NaN
# e  0.168444  0.284992  0.137487
# f  0.904736  0.756874  0.819553
# '''
#
# # 检查每列的数据是否存在缺失,返回True/False
# df3['one'].isnull()
# ''''
# a    False
# b     True
# c    False
# d     True
# '''
#
# # 缺失数据的计算,求和数据时,NaN将被视为0; 如果数据全部是NaN,那么结果将是NaN
# df3['one'].sum()
#
# # 使用指定数据来替换NaN值
# '''
#  DataFrame.fillna（value = None,method = None,axis = None,inplace = False,limit = None,downcast = None,** kwargs ）
#  使用指定的方法和数据填充NA/NaN值,
#  Value表示填充数据,
#  method表示填充方法（'backfill','bfill','pad','ffill',None）
# '''
# df3.fillna(0)
# '''
#         one       two     three
# a  0.896954  0.004486  0.398638
# b  0.000000  0.000000  0.000000
# c  0.011506  0.058437  0.850751
# d  0.000000  0.000000  0.000000
# e  0.473934  0.642129  0.368234
# f  0.895597  0.313774  0.140006
# g  0.000000  0.000000  0.000000
# h  0.126904  0.620270  0.813192
# '''
#
# # 删除带有NaN的数据
# '''
# DataFrame.dropna（axis = 0,how ='any',thresh = None,subset = None,inplace = False ）
#  How表示删除的方式（any：删除存在NA值的行或列；all：删除整行/列全部都为NA的列或行）
# '''
# df3.dropna()
#
# # """  =====================  pandas数据的输入输出"""
# print("****" * 30)
# # """  =====================  pandas数据的输入输出"""
# # """  =====================  pandas数据的输入输出"""
"""  =====================  pandas数据的输入输出"""

"""
函数	说明
read_csv	从文件、URL、文件型对象中加载带分隔符的数据. 默认分隔符为逗号
read_table	从文件、URL、文件型对象中加载带分隔符的数据. 默认分隔符为制表符（"\t"）
read_fwf	读取定宽列格式数据（即 无分隔符）
read_clipboard	读取剪贴板中的数据,可以看作read_table的剪贴板版. 再将网页转换为表格时很有用
read_excel	从Excel XLS 或xlsx file 读取表格数据
read_html	读取HTML文档中的所有表格
read_json	读取JSON字符串中的数据
read_pickle	读取Python pickle格式中存储的任意对象
read_sql	（使用SQLAlchemy）读取SQL查询结果为pandas的DataFrame
read_feather	读取Feather二进制文件格式
"""

# # ====================  读写csv文件  =======================
#
# # 读取csv文件
# r = pd.read_csv("test.csv",
#                 sep="\t",  # 指定分隔符
#                 names=['A', 'B', 'C', 'D', 'E'],  # 修改头表对应的列名,空列用NaN代替
#                 index_col='D',  # 指定索引列
#                 header='infer',  # 将文件第一行默认为列名
#                 encoding='utf-8',  # 指定编码格式
#                 )
#
# # 写入csv文件
# r.to_csv(
#     "re_test.csv",
#     sep='\t',  # 指定分隔符
#     mode='w',  # 写入模式
#     columns=['A', 'B', 'C'],  # 指定写入的列,若读取时D列指定为索引列,则写入时D列不存在
#     index_label='label',  # 指定索引名称
# )
#
#
# # ====================  读写excel文件  =======================
#
# # 读取excel文件
# e = pd.read_excel("test.xlsx",
#                   sheet_name='Sheet3',  # 指定工作表
#                   names=['A', 'B', 'C', 'D', 'E', 'F', 'G'],  # 修改头表对应的列名,空列用NaN代替
#                   # header=0, # 指定列名
#                   # index_col=None,  # 指定索引列
#                   )
#
# # 写入excel文件
# e.to_excel(
#     "re_test.xlsx",
#     sheet_name='Sheet3',  # 指定工作表
#     columns=['A', 'B', 'C', ],  # 指定写入的列,若读取时D列指定为索引列,则写入时D列不存在
#     index_label='序号',  # 指定索引名称
# )

# data = np.arange(15).reshape([3, 5])
# df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D', 'E'])
# # 可以通过行号和标签索引
#
#
# # 只能通过行号索引,获取一行的数据
# df.iloc[1]
#
# print(df.loc[::,'A'])

# s1 = pd.Series([1, 2, -9], index=['a', 'b', 'c'])
# s2 = pd.Series([1, 34, 434, 3], index=['a', 'f', 'b', 'n'])
# print(s1 + s2)
# '''
# a      2.0
# b    436.0
# c      NaN
# f      NaN
# n      NaN
# '''

# df = pd.DataFrame(np.arange(9).reshape([3, 3]), columns=['A', 'B', 'C'])
# func = lambda x: x.sum()
# reslut = df.apply(func)
# print(reslut)


# ====================  索引排序  =======================
'''
 根据任意一个轴上的索引进行排序,默认按升序,指定ascending=False为降序
'''
# df = pd.DataFrame(np.arange(8).reshape([2, 4]), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
# print(df)
# '''
#        d  a  b  c
# three  0  1  2  3
# one    4  5  6  7
# '''
# # 对索引列的名字进行排序
# print(df.sort_index(ascending=False))
# '''
#        d  a  b  c
# one    4  5  6  7
# three  0  1  2  3
# '''
# # 对字段列的名字进行排序
# print(df.sort_index(axis=1, ascending=False))
# '''
#        a  b  c  d
# three  1  2  3  0
# one    5  6  7  4
# '''

df = pd.DataFrame(np.arange(9).reshape([3, 3]), columns=['A', 'B', 'C'])
print(df.reset_index())
'''
   index  A  B  C
0      0  0  1  2
1      1  3  4  5
2      2  6  7  8
'''
