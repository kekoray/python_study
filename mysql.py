#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

conn_obj = pymysql.connect(
    host='koray2021.ml',
    port=9906,
    user='root',
    password='qwer9999',
    database='pymysql_db',
    charset='utf8'
)

cursor = conn_obj.cursor(
    cursor=pymysql.cursors.DictCursor
)


# 拼接查询语句,属于典型的SQL注入问题
sql = "select * from userinfo where name='%s' and password='%s';" % (name, password)
cursor.execute(sql)


# 解决SQL注入的问题只需过滤掉特殊符号，execute方法自带校验SQL注入问题，自动处理特殊符号
sql = "select * from userinfo where name=%s and password=%s;"
cursor.execute(sql, (name, password))



# # 打开数据库连接
# db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )
# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
# print "Database version : %s" % data
# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
#           VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()
# # 关闭数据库连接
# db.close()
