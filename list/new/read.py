# -*- coding: utf-8 -*- 
# @Time : 2021/8/9 11:34
# @Author : koray
# @File :
from typing import Any, Tuple

# import cv2
#
# '''
# book.txt内容:
# 1234567890
# qwertyuiop
# asdfghjkl
# zxcvbnm
# 1234567
# 2wsx3edc
# '''
#
# ''' ==================== r模式读取 ==================== '''
# # 读取模式
# f = open('book.txt', 'r', encoding="utf8")
# # 读取全部内容
# print(f.read())
# # 返回文件中的制定大小的内容
# print(f.read(10))  # 1234567890
# # # 一次只读一行
# print(f.readline())  # 1234567890
# # # 按行读取所有,返回列表,每一项为一个f.readline()
# print(f.readlines())  # ['qwertyuiop\n', 'asdfghjkl\n', 'zxcvbnm\n', '1234567\n', '2wsx3edc']
# # # 返回当前文件读取位置
# print(f.tell())  # 61
# f.close()
#
# ''' ==================== w/a模式写入 ==================== '''
# # 覆盖写入
# # overwrite = open('book.txt', 'w', encoding="utf8")
# # 追加写入
# update = open('book.txt', 'a', encoding="utf8")
# # 写入字符串数据
# update.write("\twrite... \n")
# # 定位文件读写位置,off表示偏移量,where为0表示起始位置开始,1表示当前位置,2表示结尾位置
# print(update.seek(3, 0))
# # 将缓存内容写入硬盘
# update.flush()
# # 关闭文件
# update.close()
#
# ''' ==================== with: 上下文管理器 ==================== '''
# # with: 上下文管理器,自动关闭文件,不需要调用close
# with open('book.txt', 'r', encoding="utf8") as r:
#     print(r.read())

# 常见文件格式操作

''' ==================== open模块读取图片 ==================== '''
# open模块读取文本以外的文件,读取模式是rb的二进制读取方式,返回二进制数据
# bytes类型是指一堆字节的集合,在python中以b开头的字符串都是bytes类型
with open('a.png', 'rb') as pr:
    print(pr.read())  # 二进制数据  ==>  b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00

''' ==================== cv2模块读取图片的像素矩阵 ==================== '''
# cv2模块获取图片的像素矩阵
# 安装cv2库 : pip install opencv-python
import cv2

img = cv2.imread('a.png')
print(img)
'''
[[[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [255 255 255]
  [255 255 255]]
'''

''' ==================== 读取音频文件 ==================== '''
# open模块读取文本以外的文件,读取模式是rb的二进制读取方式,返回二进制数据
with open("music.wav", "rb") as f:
    print(f.read())  # b'\x00\x00\x00\x18ftypmp42\x00\x00\x00

# 获取音频的矩阵
from scipy.io import wavfile

wav = wavfile.read("music.wav")
# print(wav)
'''
(48000, array([[   0,    0],
       [   0,    0],
       [   0,    0],
       ...,
       [-116, -116],
       [-116, -116],
       [-114, -114]], dtype=int16))
'''

''' ==================== 读取csv格式 ==================== '''
import pandas as pd
from datetime import datetime

'''
1.csv文件有表头并且是第一行,那么names和header都无需指定;
2.csv文件有表头,但表头不是第一行,需要指定header,参数从0开始;
3.csv文件有表头,但想自定义表头,同时使用names和header即可;
4.csv文件没有表头且纯数据,使用names生成表头;
'''
csv2 = pd.read_csv("test.csv", encoding="GBK",
                   sep="\t",  # 分隔符
                   names=["编号", "名字", "年龄", "地址", "日期"],  # 生成表头
                   header=0,  # 指定表头列
                   usecols=["编号", "名字", "年龄", "日期"],  # 只获取指定的列
                   index_col="编号",  # 指定索引列

                   # ================ 不常用操作 =======================
                   dtype={"编号": str},  # 指定列的类型
                   converters={"年龄": lambda x: int(x) + 10},  # 读取文件时,对指定列进行数据处理操作
                   # nrows=1,  # 一次性读取文件的行数,常用于看大文件的字段内容
                   na_values={"名字": "kk", "日期": datetime},  # 指定某列的某内容为NaN
                   verbose="true",  # 打印额外信息

                   # ================ 日期处理 =======================
                   parse_dates=["日期"],  # 指定某列为时间类型,配合date_parser使用
                   date_parser=lambda x: datetime.strptime(x, "%Y年%m月%d日"),  # 解析日期格式
                   infer_datetime_format="true"  # 设置为true,date_parser的解析性能提高
                   )
