# -*- coding: utf-8 -*- 
# @Time : 2021/8/24 11:18
# @Author : koray
# @File :

"""
请求URL的获取思路:

    1.从页面找到数据来源的url
    url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%E7%BE%8E%E5%9B%BD&'

    2.解析url传入的参数
    parse.unquote(url)
    ==>  https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=美国&

    3.设置url+?+键值对的拼接形式,从而动态传参获得对应的数据
    URL = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%s&'
"""

import requests
from urllib import parse
import json
import pandas as pd
import matplotlib.pyplot as plt

# 请求URL
_URL = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%s&'
_URL2 = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list'

# 游览器的请求头信息
_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Origin': 'https://news.qq.com',
    'Referer': 'https://news.qq.com/'
}


# url拼接参数方式爬取
def get_respones_url(country):
    # 1.将参数转化为字符类型并传入
    url = _URL % (parse.quote(country))
    print("爬取URL : ", url)
    respones = requests.get(url, headers=_headers)
    return respones


# 请求参数传入方式爬取
def get_respones_para(country):
    # 1.将参数转化为字符类型并传入
    url = _URL2
    print("爬取URL : ", url)
    # 2.请求参数
    data = {"country": country, }
    respones = requests.post(url, data=data, headers=_headers)
    return respones


if __name__ == "__main__":

    try:
        # country = input("请输入查询国家 : ")
        country = "美国"
        res = get_respones_para(country)
        # print(res.text)
        """ 
        {"ret": 0, "info": "", 
        "data": [
            {  "y": "2020","date": "01.28","confirm_add": 0,"confirm": 5,"heal": 0,"dead": 0},
            { "y": "2020","date": "01.29","confirm_add": 0,"confirm": 5,"heal": 0,"dead": 0 },
            { "y": "2020","date": "01.30","confirm_add": 1,"confirm": 6,"heal": 0,"dead": 0 }
            ...   ]
        }
        """

        # 判断请求是否成功
        if res.status_code == requests.codes.ok:
            # 将数据解析成json数据
            data = json.loads(res.text)
            # 获得json中data属性数据
            # print(data['data'])
            """ 
            [
            {  "y": "2020","date": "01.28","confirm_add": 0,"confirm": 5,"heal": 0,"dead": 0},
            { "y": "2020","date": "01.29","confirm_add": 0,"confirm": 5,"heal": 0,"dead": 0 },
            { "y": "2020","date": "01.30","confirm_add": 1,"confirm": 6,"heal": 0,"dead": 0 }
            ...   ]
            """

            # 转为DataFrame类型
            df = pd.DataFrame(data['data'])
            # print(df)
            """ 
                    y   date  confirm_add   confirm      heal    dead
            0    2020  01.28            0         5         0       0
            1    2020  01.29            0         5         0       0
            2    2020  01.30            1         6         0       0
            ..    ...    ...          ...       ...       ...     ...
            [553 rows x 6 columns]
            """

            # 设置画布大小
            plt.figure(figsize=(10, 8))
            # X轴:要与数据行数一致   Y轴:某个列字段
            plt.plot([i for i in range(576)], df["confirm"])
            plt.show()

        else:
            print("Request Error to :", res.status_code)
            exit()

    except Exception as e:
        print("异常捕获信息 : ", e)
