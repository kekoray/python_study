# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 14:50
# @Author : koray
# @File :

import re

'''=============  re模块 =============='''

# 匹配以给定条件开头的字符串,失败返回none,通过调用group()方法得到匹配的字符串
re.match("www", "www.koray2021.ml").group()  # www
re.match("www", "www.koray2021.ml").span()  # 匹配到的区间下标  ==>  (0, 3)


# 扫描整个字符串并返回第一个成功的匹配,通过调用group()方法得到匹配的字符串
re.search("www", "yuiwwwyuiswww.ml")
re.search("www", "yuiwwwyuiswww.ml").group()  # www
re.search("www", "yuiwwwyuiswww.ml").span()  # (3, 6)

# 查找所有的符合条件的文本
re.findall("w", "adjawadjw79w")  # ['w', 'w', 'w']

# 字符串替换
re.sub(r"\d+", "101", "abc = 22")  # abc = 101

# 字符串切割
re.split("\.", "www.koray2021.ml")  # ['www', 'koray2021', 'ml']

# 编译正则表达式,获得一个正则表达式对象,即提前写好正则规则
pattem = re.compile("\.")
pattem.split("www.koray2021.ml")  # ['www', 'koray2021', 'ml']
pattem.search("www.koray2021.ml").group()



# # 正则表达式修饰符  todo : "???
# # 正则表达式可以包含一些可选标志修饰符来控制匹配的模式,修饰符被指定为一个可选的标志
# # re.I对大小写不敏感
# re.match("life is short", "Life is short, you need Python", flags=re.I).group()  # Life is short

'''=============  正则表达式基础  =============='''

# 使用[]指定匹配元素的范围, {}指定匹配次数
re.findall(r'[0-9]{1,3}', "qeqw123ytu3792")  # ['123', '379', '2']
# 使用\d (小写)匹配数字
re.findall(r'\d+', "qeqw123ytu3792")  # ['123', '3792']
# 使用\D (大写)匹配任意的非数字字符
re.findall(r'\D+', "qeqw123ytu你好世界")  # ['qeqw', 'ytu你好世界']

# 使用\w (小写)匹配数字字母下划线
re.findall(r'\w+', "qeqw~.;[ps]\=|123ytuc 你好世界37adw_ee43")  # ['qeqw', 'ps', '123ytuc', '你好世界37adw_ee43']
# 使用\W (大写)匹配非数字字母下划线
re.findall(r'\W+', "qeqw~.;[ps]\=|123ytuc 你好世界37adw_ee43")  # ['~.;[', ']\\=|', ' ']

# 使用\s (小写)匹配任意空白字符
re.findall(r'\s+', "qeqw123ytu37 92_adw_ee43")
# 使用\S (大写)匹配任意非空字符
re.findall(r'\S+', "qeqw123ytu37 92_adw_ee43")  # ['qeqw123ytu37', '92_adw_ee43']

# 只匹配英文字母
re.findall(r'[A-Za-z]+', "qeqw123ytu你好世界37 92_adw_ee43")  # ['qeqw', 'ytu', 'adw', 'ee']
# 只匹配中文, \u4e00和\u9fa5 两个unicode值正好是Unicode表中的汉字的头和尾.
re.findall(r'[\u4e00-\u9fa5]{1,}', "qeqw123ytu你好世界37 92_adw_ee43")  # ['你好世界']

'''=============  正则表达式使用  =============='''

# 匹配文本信息中的邮箱信息
re.findall(r'[A-Za-z0-9]+@[A-Za-z0-9]+\.com', "我的邮箱是 python996@icu.com")

# 匹配网址URL
re.findall(r'[a-zA-z]+://[^\s]*', "我的个人主页：https://www.python.org")

# 匹配身份证号码
s = re.findall(r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)', "假的身份证:12345678901234567X")
print(s)  # [('123456', '7890', '12', '34', '567', 'X')]
print("".join(s[0]))  # '12345678901234567X'

# 匹配手机号码
re.findall(r'\d{3}\d{8}|\d{4}\{7,8}', "假的手机:13012345678")

# 匹配日期格式
re.findall(r'\d{4}-\d{1,2}-\d{1,2}', "日期是2021-02-22")

# IP地址
re.findall(r'\d{3}\.\d{3}\.\d{3}\.\d{3}', "IP地址为192.168.100.140")

# 贪婪模式下的匹配
# 尝试匹配尽可能多的字符
html = "aa<div>test1</div>bb<div>test2</div>cc "
re.search("<div>.*</div>", html).group()  # '<div>test1</div>bb<div>test2</div>'

# 非贪婪模式下的匹配
# 尝试匹配尽可能少的字符,需要在表达式的"*","?","+","{m,n}"后面加上?实现非贪婪模式
html = "aa<div>test1</div>bb<div>test2</div>cc "
re.search("<div>.*?</div>", html).group()  # '<div>test1</div>'
