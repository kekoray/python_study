# -*- coding: utf-8 -*- 
# @Time : 2021/8/24 11:18
# @Author : koray
# @File :

import requests

# =============== 参数设置 ====================
# 请求URL
url = 'https://fanyi.baidu.com'
# 请求参数
data = {'from': 'zh',
        'to': 'en',
        'query': '人生苦短'
        }
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', }
# 代理ip
proxies = {"http": "http://100.10.1.10:3128", "https": "http://100.10.1.10:1080"}


""" ================  get 请求"""
response1 = requests.get(url,  # 请求url
                        params=data,  # 请求参数
                        headers=headers,  # 请求头
                        proxies=proxies,  # 代理ip
                        timeout=5,  # 超时参数
                        verify=True  # 避免ssl证书问题
                        )


""" ================  post 请求"""
response2 = requests.post(url,
                         data=data,
                         headers=headers,
                         proxies=proxies
                         )

print(response2.status_code)
