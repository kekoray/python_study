# python学习





## 基础语法与编码规范



### 编码

给源码文件指定不同的编码.

```python
# -*- coding: utf-8 -*-
# -*- coding: cp-1252 -*-
```



### 标识符

标识符由字母,下划线和数字组成, 第一个字符必须是字母或下划线组成, 区分大小写, 也不能使用python的关键字.

```python
import keyword
keyword.kwlist   #查看关键字
```

> ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']



### 行与缩进

- 同一个代码块的语句必须包含相同的缩进空格数(一般为4个空格), 否则会报错.
- 函数和类的定义, 代码前后都要用2个空行进行分割

```python
if True:
    print ("True")
else:
    print ("False")
```



### 多行语句

使用反斜杠( \\ )来实现多行语句, 或者在 [ ] , { } , ( ) 的代码块中使用逗号实现多行语句.

```python
_str = '123456789' \
       '22222'
    
_str2 = ['123456789',
         '22222']
```



### 工具包引入

```python
import package
import package as pk
from package import function_xx
```





## 基本数据类型



### 数值类型

python中数字有四种类型：整数、布尔型、浮点数和复数.

- `int` (整数), 只有一种整数类型int, 表示为长整型. 
- `bool` (布尔), 如 True.
- `float` (浮点数), 如 1.23, 3E-2.
- `complex` (复数), 如 1+2j, 1.1+2.2j.



#### complex

complex复数类型, 由(real实部+imag虚部+虚部后缀j)组成;

complex(real,imag)函数用于创建一个复数或者将一个数或字符串转换为复数形式, 其返回值为一个复数, 用c.real和c.imag来取两部分数据; 

real可以为int,long,float或字符串类型; 而image只能为int,long,或float类型; 如果第一个参数为字符串,第二个参数必须省略; 若第一个参数为其他类型,则第二个参数可以选择;

```python
a = 2
b = 232
e = complex(float(a), float(b))
print id(a)  # 获得对象的id标识
print ['a:', type(a), 'b:', type(b), 'e:', type(e)]  # 获取当前数据的数据类型
print e  # (2+232j)
print e.real  # 2.0
print e.imag  # 232.0
```



### 数值运算符

| 运算符                                                       | 描述                           |
| ------------------------------------------------------------ | ------------------------------ |
| `[]` `[:]`                                                   | 下标，切片                     |
| `**`                                                         | 指数                           |
| `~` `+` `-`                                                  | 按位取反, 正负号               |
| `*` `/` `%` `//`                                             | 乘，除，模，整除               |
| `+` `-`                                                      | 加，减                         |
| `>>` `<<`                                                    | 右移，左移                     |
| `&`                                                          | 按位与                         |
| `^` `|`                                                      | 按位异或，按位或               |
| `<=` `<` `>` `>=`                                            | 小于等于，小于，大于，大于等于 |
| `==` `!=`                                                    | 等于，不等于                   |
| `is` `is not`                                                | 身份运算符                     |
| `in` `not in`                                                | 成员运算符                     |
| `not` `or` `and`                                             | 逻辑运算符                     |
| `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` ` | =` `^=` `>>=` `<<=` |                                |



### 字符串

定义字符串可以使用单引号,双引号,三引号等三种方式.

单引号,双引号创建的只能是单行的字符串; 三引号可创建多行的字符串.

字符串的截取语法 :  变量[开始下标 : 结束下标 : 步长]

字符串有两种索引方式, 从左往右以0开始, 从右往左以-1开始.

字符串内容为浮点型要转换为整型时, 要先转化成float再转换成int.

斜杠可以用来转义, 使用r可以让反斜杠不发生转义.

受保护的实例属性用单个下划线开头.

私有的实例属性用两个下划线开头.

```python
# 定义字符串
_str = '123456789'

# 字符串的截取语法 : 变量[开始下标 : 结束下标 : 步长]
print(_str[0:8:2])  # 输出第1个开始到第8个且每隔1个字符
print(_str[0:-1])   # 输出第1个到倒数第2个的所有字符

# 字符串内容为浮点型要转换为整型时,要先转化成float再转换成int
print(int(float("2.1")))

# 斜杠可以用来转义, 使用r可以让反斜杠不发生转义.
print('\n')  # 输出空行
print(r'\n')  # 输出 \n
```



### 格式化字符串方式

```python
# 1.占位符形式   %s(字符串),%d(整型),%f(浮点)
print('abc + %d' % 2)
print('abc + %s' % 'cc')

# 2.format()形式
print('abc + {0}'.format('kk', 2))

# 3.加号+形式, 前后都只能是string
print('abc' + '2')

# 4.逗号,形式
print('abc', 'def')

# 5.f形式
a = 'def'
print(f'abc + {a}')
```



### 类型转换

- `int( )` ：将一个数值或字符串转换成整数
- `float( )` ：将一个字符串转换成浮点数
- `str( )` ：将指定的对象转换成字符串形式
- `chr( ) `：将整数转换成该编码对应的字符串(一个字符)
- `ord( )` ：将字符串(一个字符)转换成对应的编码(整数)



### 空值

空值是Python里一个特殊的值, 用`None`表示.



### 列表

list是一种有序可重复的集合，可以随时添加和删除其中的元素.

```python
a = list() # 创建空列表
a = ['Michael', 'Bob', 'Tracy']   # 创建列表

a[-1]  # 获取最后一个元素
a.append('Adam')  # 追加元素到末尾
a.insert(1, 'Jack') # 把元素插入到指定的位置
a.pop(1) # 删除指定位置的元素
a[1] = 'Sarah' # 把某个元素替换成别的元素
```



### 元组

tuple是一种有序的列表, 一旦初始化就不能修改tuple的元素. 

能用tuple代替list就尽量用tuple, 因为代码更安全.

若tuple中某个元素为list时, 可以改变list里的元素, 但是不能改变list这个类型对象.

只有1个元素的tuple定义时必须加一个逗号`,`来消除歧义.

```python
a = tuple() # 创建空元组
a = ('Michael', 'Bob', 'Tracy')  # 创建元组
a = (1,)  # 创建1个元素的元组
a[1]  # 只能查询元素
```



### 字典

使用键值对(key-value)进行存储.

key必须是不可变对象, 如字符串, 整数等.

```python
d = dict() # 创建空字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  # 创建字典
d['kk'] = 67  # 添加元素
'kk' in d # 通过in判断key是否存在字典中
d.get('kkk',0)  # 通过get()方法判断key是否存在字典中,不存在返回none,或者指定返回值
d.pop('kk') # 删除key
```



### 集合

set是一种无序无重复的集合

```python
s = set()    # 创建空集合
s = {1,2,3}  # 创建集合
s.add(4) 	 # 添加元素
s.remove(4)   # 删除元素
```





## 控制语句



### if判断

从上往下判断,如遇到true就执行当前代码,忽略后面代码.

```python
a = 2
if a > 3:
    print('OK')
elif a == 2:
    print('yes')
else:
    print('no')
```

缩写形式, 只要x是非零数值,非空字符串,非空list等, 就判断为True.

```python
x = 2
if x :
    print('This is no none.')
```





### for循环

```python
sum = 0
for x in range(11):   # range(11)表示生成1到10的整数
    sum+=x
    print(sum)  # 每次循环都执行
print(sum)  # 打印sum最终结果
```

range函数用法

```python
range(101)        #  产生0到100范围的整数,需要注意的是取不到101.
range(1, 101)     #  产生1到100范围的整数,相当于前面是闭区间后面是开区间.
range(1, 101, 2)   #  产生1到100的奇数,其中2是步长,即每次数值递增的值.
range(100, 0, -2)  #  产生100到1的偶数,其中-2是步长,即每次数字递减的值
```



### while循环

```python
sum = 0
a = 10
while a > 0 :
    print('OK --> ' + str(a))
    sum+=a
    a-=2
print(sum)
```



### break

提前退出循环.

```python
n = 1
while n <= 100:
    if n > 10: # 当n = 11时,条件满足,执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
```



### continue

跳过当前的这次循环.

```python
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数,执行continue语句
        continue # continue语句会直接继续下一轮循环,后续的print()语句不会执行
    print(n)
```







## 函数



### 函数定义

函数可以同时返回多个值,但其实就是一个tuple

函数参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

`*args`是可变参数,args接收的是一个tuple

``**kw`是关键字参数,kw接收的是一个dict

```python
def 函数名(参数):
    #方法体
    return
```

定义函数

```python
def add(*args):  
    total = 0 
    for val in args:
        total+=val
    return total
```

定义空函数

```python
def nop():
    pass  # 什么都不做
```



### 函数调用

```python
print(add(1))
print(add(1,2))
```

由于Python没有函数重载,所以每个文件就代表了一个模块(module), 在不同的模块中可有同名函数, 通过import导入指定的模块就可以使用同名函数.

> module1.py
>
> ```python
> def foo():
>     print('hello, world!')
> ```

> module2.py
>
> ```python
> def foo():
>   print('goodbye, world!')
> ```

函数调用

```python
from module1 import foo
foo() # 输出hello, world!

from module2 import foo
foo() # 输出goodbye, world!
```







## Py2与Py3的区别点



### 1. 默认的编码不同

py2默认编码为ascii, py3默认编码为utf-8

故py2使用中文时,需要在py文件第一行注释  `# -*- coding: utf-8 -`



### 2. print语句不同

```python
print "hello!"   # py2独有,可不用括号
print("hello!")  # py2与py3都能用
```



### 3. input语句不同

py3中从input输入的均为string类型,如果需要整形或浮点型需要强转;

> `raw_input` : 获取到的输入永远都是str类型, py3就没有这个方法,已整合到input中
>
> `input` : 获取到的输入会自动判断其类型,字符格式必须加上单引号或者双引号

```python
print(int(input("请输入整数..")), type(input("随便输入..")))
```







## 其他API操作



### 文件目录操作

```python
import os
print os.getcwd()  #获取当前的文件目录结构
os.chdir("xx/xx")  #修改当前的文件目录结构,相当于复制文件
```



### 随机数生成

利用正态分布产生一些列的随机数, 模拟现实生活中一些场景 (二项分布、beta分布)

1. rendom包

```python
# 生成0-1之间的随机数
import rendom
print random.random() 取[0,1)内的随机小数
print random.randint(1,10) 取[0,10]内的随机小数
print random.randrange(1,10,2)
```

2. numpy包

```python
import numpy as np
np.random.rendom(size(3,2)) #产生0-1之间的符合均匀分布的随机数
#产生0-1之间的8个随机数
np.random.randint(1,10,8)
#产生正态分布的随机数
pn.random.randn()
pn.random.randn(2,4)  #参数表示矩阵size为2行4列
#产生二项分布的随机数
np.random.binomial(10,0.5,(2,3)) #第一个参数表示均值,二表示方差,三表示矩阵的size
# 产生卡方分布的随机数
np.rendom.chisquare(2,(2,3)) #第一个参数表示自由度
#gama伽马分布
np.random.gamma(2,4,100) #前两个参数表示自由度
```







## python整合hive案例

> 使用pyhive库来连接hive server2提供的对外接口, 使用sql语句来对数据进行查询, 并处理返回结果.



### 1. 安装依赖

```python
pip install sasl
pip install thrift
pip install thrift-sasl
pip install PyHive
```



### 2. 代码演示

```python
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
    # 调用
    dhive()


```





