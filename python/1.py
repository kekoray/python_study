# -*- coding: utf-8 -*-     python2的utf-8注释
# @Time : 2021/6/22 16:37
# @Author : koray
# @File :

import requests
r = requests.get('https://www.baidu.com')
r.text()
r.url()
r.encoding()

print "hello!"
