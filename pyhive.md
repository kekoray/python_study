



## 使用PyHive库链接hive

> https://github.com/dropbox/PyHive



安装依赖包

```
pip install sasl
pip install thrift
pip install thrift-sasl
pip install PyHive
```



代码演示

```python
from pyhive import hive   

conn = hive.Connection(host='****', port=****, username='****', database='****')
cursor.execute(''SELECT * FROM my_awesome_data LIMIT 10'')
for i in range(****):
    sql = "INSERT INTO **** VALUES ({},'username{}')".format(value, str(username))
    cursor.execute(sql)
 

# 下面是官网代码：
from pyhive import presto  # or import hive
cursor = presto.connect('localhost').cursor()
cursor.execute('SELECT * FROM my_awesome_data LIMIT 10')
print(cursor.fetchone())
print(cursor.fetchall()) 
```



```python
from pyhive import hive

HOST="127.0.0.1"
PORT=10000
USERNAME="hadoop"
DATABASE="default"

conn=hive.Connection(host=HOST, port=PORT, username=USERNAME,database=DATABASE)
 
cursor = conn.cursor()
#cursor.execute("INSERT INTO TABLE test_out(name,count,time) SELECT name,count(1),to_date(time) FROM test GROUP BY name,to_date(time)")
cursor.execute("SELECT * FROM test")
for result in cursor.fetchall():
    print(result[2])
```





使用pyhive库来连接hive server2提供的对外接口，使用sql语句来对数据进行查询，并处理返回结果。



```
yum install python-pip gcc gcc-c++ python-virtualenv cyrus-sasl-devel
pip install pyhive
pip install thift
pip install sasl
pip install thrift-sasl
```



```
# -*- coding: utf-8 -*-
from pyhive import hive

conn = hive.Connection(host='HiveServer2 host', port=10000, username='hdfs', database='default')
cursor = conn.cursor()
cursor.execute('select * from demo_table limit 10')
for result in cursor.fetchall():
    print result
```





```
import sys
from pyhive import hive

def dhive():
    try:
        conn = hive.connect(host="server_ip",port=10000, auth="...", database="...",username="...",password="...")
        cursor = conn.cursor()
        cursor.execute("select * from table_name")
        res = cursor.fetchall()
        
        for item in res:
            print(item)
        conn.close()
    except Exception:
        print('excepion happen')
		
if __name__ == "__main__":
    dhive()
```



配置hive

```
hive_config = {
    'mapreduce.job.queuename': 'my_hive',
    'hive.exec.compress.output': 'false',
    'hive.exec.compress.intermediate': 'true',
    'mapred.min.split.size.per.node': '1',
    'mapred.min.split.size.per.rack': '1',
    'hive.map.aggr': 'true',
    'hive.groupby.skewindata': 'true'
}

conn = hive.connect(host="server_ip",port=10000, auth="...", database="...",username="...",
                    password="...", configuration=hive_config)

```



通过fetchall()取出的结果是表中单纯的数据.



获取列名

```
columns = cursor.description
col_names = []
    for column in columns:
        col_names.append(column[0])
```





> 在Cursor类中有一个description()方法，通过@property装饰器被装饰成一个属性，在这个方法下面就记录了数据表中每一列对应的列名，数据类型等信息。

```
@property
def description(self):
        """This read-only attribute is a sequence of 7-item sequences.

        Each of these sequences contains information describing one result column:

        - name
        - type_code
        - display_size (None in current implementation)
        - internal_size (None in current implementation)
        - precision (None in current implementation)
        - scale (None in current implementation)
        - null_ok (always True in current implementation)

        This attribute will be ``None`` for operations that do not return rows or if the cursor has
        not had an operation invoked via the :py:meth:`execute` method yet.

        The ``type_code`` can be interpreted by comparing it to the Type Objects specified in the
        section below.
        """
```









