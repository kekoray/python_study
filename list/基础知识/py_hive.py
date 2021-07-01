# -*- coding: utf-8 -*-

import sys
from pyhive import hive

# hive配置
hive_host = '1.15.55.232'
hive_port = '7001'
hive_username = 'root'
hive_password = 'FyTOSDYPcp42esn7'
hive_database = 'lazada_dw'
hive_confign = {
    'mapreduce.job.queuename': 'my_hive',
    'hive.execution.engine': 'tez',
    'hive.tez.container.max.java.heap.fraction': '0.9',
    'tez.am.max.app.attempts': '5',
    'tez.am.max.app.task.failed.attempts': '10',
    'hive.tez.exec.print.summary': 'true',
    'hive.merge.tezfiles': 'true',
}


def dhive():
    try:
        # 数据库连接
        conn = hive.Connection(host=hive_host, port=hive_port, username=hive_username, database=hive_database, password=hive_password, configuration=hive_confign)
        cursor = conn.cursor()
        cursor.execute('select * from demo_table limit 10')

        # 通过fetchall()取出的结果是表中单纯的数据
        for res in cursor.fetchall():
            print(res)  
        print(cursor.fetchone())
        print(cursor.fetchall()) 

        # 获取列名
        columns = cursor.description
        col_names = []
        for column in columns:
            col_names.append(column[0])

        # 关闭连接
        conn.close()
    except Exception:
        print('excepion happen')
 
		
if __name__ == "__main__":
    dhive()

