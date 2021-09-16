# -*- coding: utf-8 -*- 
# @Time : 2021/9/2 11:27
# @Author : koray
# @File :

import redis
from redis_conf import *

# 连接redis
pool = redis.ConnectionPool(host=host, port=port, password=password, decode_responses=True)
r = redis.Redis(connection_pool=pool, db=database)

if r.ping() == True:
    print("====  redis连接成功  ====")
    # 删除当前库的所有key
    r.flushdb()

else:
    print("====  redis连接失败  ====")
    exit(1)


# String类型的数据操作
def stringOperate():
    r.set("name", "张三")
    print(r.get("name"))
    r.incr("incr")
    r.decr("incr")
    r.incrby("incr", 2)
    print(r.get("incr"))
    r.close()


# hash表的操作
def hashOperate():
    r.hset("hsetkey", "jmapkey", "jmapValue")
    r.hset("hsetkey", "jmapkey2", "jmapvalue2")
    for i in r.hgetall("hsetkey"):
        print("key值为 %s , vaule值为 %s" % (i, r.get(i)))

    for _ in r.hkeys("hsetkey"):
        print("所有的key为", _)

    for _ in r.hvals("hsetkey"):
        print("所有的value值为", _)
    r.close()


# list集合操作
def listOperate():
    r.lpush("listkey", "listvalue1", "listvalue2", "listvalue3")
    for _ in r.lrange("listkey", 0, -1):
        print("所有的value值为", _)
    print(r.lpop("listkey"))
    r.close()


# 对set集合操作
def setOperate():
    r.sadd("setkey", "setvalue1", "setvalue2", "setvalue3")
    for _ in r.smembers("setkey"):
        print("所有的value值为", _)
    r.srem("setkey", "setvalue2")
    for _ in r.smembers("setkey"):
        print("所有的value值为", _)
    r.close()


# zset操作
def sortSetOperate():
    r.zadd("比武成绩", {"乔峰": 2})
    r.zadd("比武成绩", {"王重阳": 5})
    r.zadd("比武成绩", {"虚竹": 7})
    r.zadd("比武成绩", {"王语嫣": 2})
    r.zadd("比武成绩", {"段誉": 5})
    r.zadd("比武成绩", {"张三丰": 20})

    print("===========正序排序===========")
    for i in r.zrange("比武成绩", 0, -1):
        print("名字: %s, 排名：%s , 分数：%s" % (i, r.zrank("比武成绩", i), r.zscore("比武成绩", i)))

    print("===========倒序排序===========")
    for _ in r.zrevrange("比武成绩", 0, -1):
        print("名字: %s, 排名：%s , 分数：%s" % (_, r.zrank("比武成绩", _), r.zscore("比武成绩", _)))
    r.close()


if __name__ == '__main__':
    stringOperate()
    print('==' * 20)
    hashOperate()
    print('==' * 20)
    listOperate()
    print('==' * 20)
    setOperate()
    print('==' * 20)
    sortSetOperate()
    print('==' * 20)
