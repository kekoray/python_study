# -*- coding: utf-8 -*-
# @Time : 2021/8/6 17:28
# @Author : koray
# @File :
# import os
import sys
# import time
# import datetime
# import random
from ..kn.py_hive import dhive


class tool(object):
    # sys.path.append('D:\Code_Repository\python_study\list\new_kn\create_class.py')
    # # os是负责与操作系统的模块
    import os
    # # 获取当前进程 id
    # print("当前进程的 ID：", os.getpid())  # 当前进程的 ID： 9404
    # # 获取当前父进程 id
    # print("当前父进程的 ID：", os.getppid())  # 当前父进程的 ID： 6904
    # # 获取当前所在路径
    # print("当前所在路径为：", os.getcwd())  # 当前所在路径为： D:\Code_Repository\python_study\list\new_kn
    # # 改变当前工作目录
    # os.chdir("./home/")
    # print("修改后当前所在路径为：", os.getcwd())  # 修改后当前所在路径为： ./home/
    # # 返回当前目录下的所有文件
    # print("当前目录下的文件有：", os.listdir(os.getcwd()))  # 当前目录下的文件有： ['class_kn.py', 'create_class_module.py', 'tool.py']
    # # 返回当前路径下的所有文件,包括子目录文件;
    # for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    #     for name in files:
    #         print(os.path.join(root, name))
    #     for name in dirs:
    #         print(os.path.join(root, name))
    #
    # '''文件操作'''
    # # 获取当前工作目录的名称：
    # print(os.curdir)
    # # 父目录字符串名称
    # print(os.pardir)
    # # 删除指定文件
    # os.remove("../kn/abc.py")
    # # 删除文件夹
    # os.removedirs("./a")
    # # 重命名文件, rename(命名前，命名后)
    # os.rename("../kn/abc.py", "../kn/1.py")

    # ''' os.path子模块 '''
    # # 返回绝对路径
    # os.path.abspath("path")
    # # 文件存在则返回 True,不存在返回 False
    # os.path.exists("path")
    # # 返回文件大小，如果文件不存在就返回错误
    # os.path.getsize("path")
    # # 判断路径是否为文件
    # os.path.isfile("path")
    # # 判断路径是否为文件夹
    # os.path.isdir("path")
    # # 拼接路径
    # os.path.join("path", "path2")

    # # sys是负责与解释器交互的模块
    # import sys
    # # 当前程序退出,0表示正常退出,其他值表示异常退出
    # # sys.exit(0)

    # # 获取模块搜索路径
    # l = sys.path  # 返回是list
    # l.append("./Code_Repository/start")  # 添加模块的搜索路径
    # print(sys.path)

    # # 获取当前系统平台
    # print(sys.platform)  # win32

    # # 从程序外部向程序传递参数,参数以列表的形式传递,第一个为当前文件名
    # print(sys.argv[0])  # D:/Code_Repository/python_study/list/new_kn/tool.py

    # # 获取当前版本
    # print(sys.version)  # 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]

    # 获取当前编码
    # print(sys.getdefaultencoding())  # utf-8

    # # time是处理时间的模块
    # import time
    #
    # # 获取当前时间戳
    # print("时间戳：", time.time())  # 时间戳： 1628245640.3183932
    # # 获取当前时间的时间元组
    # localtime = time.localtime()
    # print("本地时间为 :", localtime)
    # ''' 本地时间为 : time.struct_time(tm_year=2021, tm_mon=8, tm_mday=6,
    #             tm_hour=18, tm_min=27, tm_sec=20, tm_wday=4, tm_yday=218, tm_isdst=0) '''
    # # 获取格式化的时间
    # print("本地时间为 :", time.asctime(localtime))  # 本地时间为 : Fri Aug  6 18:27:20 2021
    # # 接收当前时间的时间元组,并返回以可读字符串表示的当地时间,格式由参数format决定
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 2021-08-06 18:27:20

    # # datetime
    # import datetime
    #
    # datetime.date
    # datetime.time
    # datetime.datetime
    # datetime.timedelta
    #
    # randmo是提供随机函数的模块
    # import random
    #
    # # 产生1到10的一个整数型随机数
    # print(random.randint(1, 10))
    # # 产生0到1 之间的随机浮点数
    # print(random.random())
    # # 产生1.1到 5.4之间的随机浮点数,区间可以不是整数
    # print(random.uniform(1.1, 5.4))
    # # 从序列中随机选取一个元素
    # print(random.choice('tomorrow'))
    # # 生成从1到100的间隔为2的随机整数
    # print(random.randrange(1, 100, 2))
    # # 取三个值
    # print(random.sample("python", 3))
    #
    # # 洗牌，打乱序列
    # n = [1, 2, 3, 4]
    # random.shuffle(n)
    # print(n)  # [1, 4, 2, 3]
