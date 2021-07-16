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





## 数据类型



### 数据类型分类

- 有序: 可以使用下标(索引)访问元素.
- 无序: 不可以使用下标(索引)访问元素.
- 可变: 可以被修改
- 不可变: 不可以被修改

|            |     有序     |    无序    |
| :--------: | :----------: | :--------: |
|  **可变**  |     列表     | 字典, 集合 |
| **不可变** | 字符串, 元组 |    数值    |







### 1.数值

python中数字有四种类型：整数、布尔型、浮点数和复数.

> python中只有一种整数类型int.

| 类型    | 值              | 范围                     |
| ------- | --------------- | ------------------------ |
| int     | 1, 2            | (-∞, +∞)                 |
| float   | 1.2 , 3E-2      | (-∞, +∞)                 |
| bool    | true            | [true, false]            |
| complex | x+yj , 1.1+2.2j | x为实数部分, y为虚数部分 |



#### Complex

complex复数类型, 由(real实部+imag虚部+虚部后缀j)组成;

complex(real,imag)函数用于创建一个复数或者将一个数或字符串转换为复数形式, 其返回值为一个复数, 用c.real和c.imag来取两部分数据; 

real可以为int,long,float或字符串类型; 而image只能为int,long,或float类型; 

如果第一个参数为字符串,第二个参数必须省略; 若第一个参数为其他类型,则第二个参数可以选择;

```python
# 创建复数
a = 2
b = 232
e = complex(float(a), float(b))

# 获得对象的id标识
print id(a)  

# 获取当前数据的数据类型
print ['a:', type(a), 'b:', type(b), 'e:', type(e)]  

# 获取复数的虚实部分
print e  # (2+232j)
print e.real  # 2.0
print e.imag  # 232.0
```



#### 计算函数

| 函数描述               | 函数体         |
| ---------------------- | -------------- |
| 绝对值                 | abs(x)         |
| 四舍五入               | round(x)       |
| 返回两个数值的商和余数 | divmod(y,x)    |
| 求最值                 | max(x), min(x) |
| 求和                   | sum(x)         |



#### math模块常用方法

- math模块运算的是数学运算.
- cmath模块运算的是复数运算.

| 方法描述 | 方法体         |
| -------- | -------------- |
| 三角函数 | sin, cos ,tanh |
| 绝对值   | fabs           |
| 向上取整 | ceil           |
| 向下取整 | floor          |
| 获取阶乘 | factorial      |
| x的y次方 | pow            |





### 2.字符串

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



#### 索引



#### 切片



#### 常用操作

```
1.分割

2.替换

3.大写

4.小写

5.拼接
```



#### 格式化输出

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



### 3.元组

- tuple是一种有序的列表, 一旦初始化就不能修改tuple的元素. 
- 若tuple中某个元素为list时, 可以改变list里的元素, 但是不能改变list这个类型对象.

- 只有1个元素的tuple定义时必须加一个逗号`,`来消除歧义.
- 能用tuple代替list就尽量用tuple, 因为代码更安全.

```python
# 创建空元组
a = tuple() 

# 创建元组
a = ('Michael', 'Bob', 'Tracy')  

# 创建单元素元组时,后面需要加逗号消除歧义
a = (1,)  

# 可以使用索引和切片的方式取值
a[1] 

# 元组加法,拼接两个元组
b = (2,3)
a + b     # (1,2,3)

# 元组乘法,重复元素个数
b * 2     # (2,3,2,3)
```





### 4.列表

list是一种有序可重复的集合，可以随时添加和删除其中的元素.

```python
# 创建空列表
a = list() 

# 创建列表
a = ['Michael', 'Bob', 'Tracy']   

# 列表推导式创建列表
i for i in range(5)     # [0,1,2,3,4]

# 可以使用索引和切片的方式取值
a[-1] 
```



#### 常用操作

```python
# ====================  1.增加  =======================
# 追加元素到末尾
a.append('Adam') 
# 把元素插入到指定的位置
a.insert(0, 'Jack') 
# 将可迭代对象的每个元素逐个插入列表尾部
a.extend([1,2])     # ['Michael', 'Bob', 'Tracy', 1, 2]   

# ====================  2.删除  =======================
# 删除指定位置的元素,返回其值
a.pop(1)  
# 删除列表中第一个出现的给定元素
a.remove('Tracy')

# ====================  3.修改  =======================
# 把某个元素替换成别的元素
a[1] = 'Sarah' 

# ====================  4.查找  =======================
# 返回给定元素第一次出现位置的下标
a.index('Bob')     # 1

# ====================  5.排序  =======================
#对列表进行排序,默认升序
a.sort()
# 将列表中的元素进行逆置,即降序排序
a.reverse();

# ====================  6.数量统计  =======================
# 返回给定元素出现的次数
a.count('Bob')
```



#### 列表与数组关系

python中的列表与数组虽然相识, 但是两者并不是一种结构.

python的内置数据结构中没有数组, 可导入numpy包实现.

列表和数组可以相互转化, 但本质不是一样的, 打印输出的分隔符也不同.

```python
import numpy

a = [1,2,3,4]
print(a)     # [1, 2, 3, 4]  --  列表结构,逗号分割
print(numpy.array(a)     # [1 2 3 4]  --  数组结构,空格分隔
```









### 5.字典

- 字典是无序可变的序列, 使用键值对(key-value)进行存储.

- key必须是不可变对象, 如字符串, 整数等.
- 数据量大时, 字典访问速度比列表快.

```python
# 创建空字典
d = dict() 

# 创建字典
d = dict(Michael = 95, Bob = 75, Tracy = 85)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  



d['kk'] = 67  # 添加元素
'kk' in d # 通过in判断key是否存在字典中
d.get('kkk',0)  # 通过get()方法判断key是否存在字典中,不存在返回none,或者指定返回值
d.pop('kk') # 删除key
```



#### 常用操作

```python
# ====================  1.获取  =======================
# 根据键获取值,键不存在返回None.
d.get('Michael')
# 返回一个包含所有(k,v)元组的列表
d.items()
# 返回一个所有键组成的列表
d.keys()
# 返回一个所有值组成的列表
d.values()

# ====================  2.添加  =======================
# 若k不存在,则添加kv对; 若k已存在,则修改v
d['kk'] = 67  

# ====================  3.更新  =======================
# 使用dict1对字典进行更新
dict1 = {'a' : 1, 'Tracy': 2}
d.update(dict1)     # {'Michael': 95, 'Bob': 75, 'Tracy': 2, 'a': 1}

# ====================  4.删除  =======================
# 删除并返回k对应的值
d.pop('a')
# 随机删除并返回一个kv对
d.popitem()
# 清空字典,返回一个空字典; 与del()删除字典区分
d.clear()
```



### 6.集合

Set是一种无序无重复的序列, 一般多用于去重操作.

```python
# 创建空集合
s = set()   

# 创建集合
s = {1,2,3}  
```



#### 常用操作

```python
# ====================  1.添加  =======================
# 添加元素
s.add(4)
# 添加对象,可以是列表,字典等,多个对象用逗号隔开
s2 = {4,5}
s.update(s2)     # {1, 2, 3, 4, 5}

# ====================  2.删除  =======================
# 移除元素,不存在的元素会报错
s.remove(5)
# 删除元素
s.discard(2)
# 随机删除一个元素
s.pop()
# 清空集合
s.clear()
```



#### 去重操作

```python
a = [1,2,3,4,5,1,2,4,3]
a = set(a)     # {1, 2, 3, 4, 5}
a = list(a)    # [1, 2, 3, 4, 5]  
```





逻辑运算

```python
交集 set1 & set2  两个集合中相同的元素
对称差集  set1 ^ set2  两个集合中不同的元素
并集 set1 | set2  两个集合内总共的元素,重复删除
差集 set1 - set2  集合1中包含而集合2中不包含的元素
```













### 数据拷贝

在python中变量名是对于数据的引用, 而数据拷贝就是解决数据引用的问题.

数据拷贝可以根据拷贝形式不同分为浅拷贝和深拷贝

- 浅拷贝, 作用于表面结构的数据拷贝.
- 深拷贝, 作用于嵌套结构中深层结构的数据拷贝.

```python
# 数据引用
L1 =[1,2,[3,4,5]]
L2 = L1
L2[0]=6
print('L1:' ,L1)     # [6, 2, [3, 4, 5]] 
print('L2:' ,L2)     # [6, 2, [3, 4, 5]] 

# 浅拷贝,使用copy()实现
L1 =[1,2,[3,4,5]]
L2 = L1.copy()
L2[0]=6
print('L1:' ,L1)     # [1, 2, [3, 4, 5]] 
print('L2:' ,L2)     # [6, 2, [3, 4, 5]] 
()
# 深拷贝,导入copy包中的deepcopy()实现,一般使用这种方式.
import copy
L1 =[1,2,[3,4,5]]
L2 =copy.deepcopy(L1)
L2[2][0] = 6
print('L1:' ,L1)     # [1, 2, [3, 4, 5]]
print('L2:' ,L2)     # [1, 2, [6, 4, 5]]
```



### 运算符

| 运算符                                         | 描述       |
| ---------------------------------------------- | ---------- |
| `+`  `-` `*`  `/`  `%`  `//`  `**`             | 算术运算符 |
| `=   +=`  `-=`  `*=`  `/=`  `//=`  `%=`   `*=` | 赋值运算符 |
| `<=`  `<`  `>`  `>=`  `= =`  `!=`              | 比较运算符 |
| `&` `^` `|` `~` `>>` `<<`                      | 位运算符   |
| `is`, `is not`                                 | 身份运算符 |
| `in` , `not in`                                | 成员运算符 |
| `and`,  `not`, `or`                            | 逻辑运算符 |







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





