# -*- coding: utf-8 -*- 
# @Time : 2021/6/22 17:42
# @Author : koray
# @File : py2与py3的不同点


# 1. input输入语句不同
# py3中从input输入的均为string类型,如果需要整形或浮点型需要强转;
# raw_input:获取到的输入永远都是str类型,py3就没有这个方法,已整合到input中
# input:获取到的输入会自动判断其类型,字符格式必须加上单引号或者双引号
print(int(input("请输入整数..")), type(input("随便输入..")))

