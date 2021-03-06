# python学习



## Py2与Py3的区别



### 1. 默认的编码不同

py2默认编码为ascii, py3默认编码为utf-8

故py2使用中文时,需要在py文件第一行注释  `# -*- coding: utf-8 -`

```python
# -*- coding: utf-8 -*- 
# @Time : 2021/8/24 11:18
# @Author : koray
# @File :
```



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





## 基础语法与编码规范

### 编码

给源码文件指定不同的编码.

```python
# -*- coding: utf-8 -*-
# -*- coding: cp-1252 -*-
```



### 变量标识符

python中的变量标识符是对数据存储地址的引用.

变量标识符由字母,下划线和数字组成, 第一个字符必须是字母或下划线组成, 区分大小写, 也不能使用python的关键字.

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



### 模块导入

```python
import package
import package as pk
from package import function_xx
```



### 基础函数

| 函数  | 作用                              |
| ----- | --------------------------------- |
| print | 用于输出, 可以通过end制定结尾符号 |
| input | 用于接收键盘输入                  |
| help  | 查看对象的帮助信息                |
| dir   | 返回对象的属性和方法列表          |
| id    | 查看对象内存地址                  |
| type  | 查看对象类型                      |







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

字符串是有序且不可变的序列.

定义字符串可以使用单引号,双引号,三引号等三种方式.

单引号,双引号创建的只能是单行的字符串; 三引号可创建多行的字符串.

> python中没有char字符类型, 单个字符被认作长度为1的字符串.

```python
# 定义字符串
_str = '123456789'
_str2 = '''12345
6789'''

# 获取长度
len(_str)

# 字符串内容为浮点型要转换为整型时,要先转化成float再转换成int
print(int(float("2.1")))
```



#### 转义字符

可以使用反斜杠对特殊符号进行转义使用.

在字符串前面加r或者R, 可以让反斜杠不发生转义.

```python
# 反斜杠可以用来转义
a = "这是\"皇帝\""
print(a)     # 这是"皇帝"

# 使用r可以让反斜杠不发生转义.
print('\n')  # 输出空行
print(r'\n')  # 输出 \n
```

| 符号 | 作用                     |
| ---- | ------------------------ |
| `\n` | 换行                     |
| `\t` | 水平制表符(HT)           |
| `\\` | 代表一个反斜线字符 “ \ ” |
| `\0` | 空字符                   |
| `\v` | 垂直制表(VT)             |



#### 索引

根据元素对应的下标(索引)获取字符串中的字符元素, 正向访问的下标从0开始, 逆向访问从-1开始.

```python
# 访问元素
_str = '123456789'
_str[2]     # 3
```



#### 切片

批量获取字符的方法 :     字符串[开始下标 : 结束下标 : 步长]

```python
# 字符串的截取语法 : 变量[开始下标 : 结束下标 : 步长]
print(_str[::])     # 输出所有
print(_str[0:8:2])  # 输出第1个开始到第8个且每隔1个字符
print(_str[0:-1])   # 输出第1个到倒数第2个的所有字符
```



#### 常用操作

```python
# 1.分割
"python".split("h")     # ['pyt', 'on']

# 2.替换
"python".replace("py","kk")     # 'kkthon'

# 3.大写
"python".lower()

# 4.小写
"python".upper()

# 5.拼接
"python".join("1234")     # '1python2python3python4'
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



#### string模块

在python3中的string模块提供的方法, 和字符串内置的方法相似度较高.

```python
import string
print(dir(string))

['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass','__all__',
 '__builtins__', '__cached__', '__doc__', '__file__', '__loader__','__name__', 
 '__package__', '__spec__', '_re', '_sentinel_dict', '_string', 'ascii_letters', 
 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 
 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
```





### 3.元组

tuple是一种有序的列表, 一旦初始化就不能修改tuple的元素. 

若tuple中某个元素为list时, 可以改变list里的元素, 但是不能改变list这个类型对象.

只有1个元素的tuple定义时必须加一个逗号`,`来消除歧义.

能用tuple代替list就尽量用tuple, 因为代码更安全.

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

list是一种有序可变的序列, 可以随时添加和删除其中的元素.

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
# 返回索引数值
len(a)

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

- key必须是不可变且唯一的, 如字符串, 整数等.
- 数据量大时, 字典访问速度比列表快.

```python
# 创建空字典
d = dict() 

# 创建字典
d = dict(Michael = 95, Bob = 75, Tracy = 85)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}   
```



#### 常用操作

```python
# ====================  1.获取  =======================
# 根据键获取值,键不存在返回None.
d.get('Michael')
d['Michael']
# 获取某个key
tuple(data.keys())[0]  # Michael
# 返回一个包含所有(k,v)元组的列表
d.items()
# 返回一个所有键组成的列表
d.keys()
# 返回一个所有值组成的列表
d.values()
# 通过in判断key是否存在字典中
'kk' in d 

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

# ====================  3.去重  =======================
a = [1,2,3,4,5,1,2,4,3]
a = set(a)     # {1, 2, 3, 4, 5}
a = list(a)    # [1, 2, 3, 4, 5]  
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
| `<=`  `<`  `>`  `>=`  `==`  `!=`               | 比较运算符 |
| `&` `^` `|` `~` `>>` `<<`                      | 位运算符   |
| `is`, `is not`                                 | 身份运算符 |
| `in` , `not in`                                | 成员运算符 |
| `and`,  `not`, `or`                            | 逻辑运算符 |





### 类型转换

| 方法       | 作用                                                    |
| ---------- | ------------------------------------------------------- |
| `int( )`   | 将一个数值或字符串转换成整数.                           |
| `float( )` | 将一个字符串转换成浮点数.                               |
| `str( )`   | 将指定的对象转换成字符串形式.                           |
| `chr( ) `  | 用一个范围在(0～255)编码整数作参数, 返回一个对应的字符. |
| `ord( )`   | 将一个字符转换成对应的编码整数.                         |







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

可以在for循环后面加else语句块, 在循环结束时执行.

```python
sum = 0
for x in range(11):   # range(11)表示生成1到10的整数
    sum+=x
    print(sum)  # 每次循环都执行
else:
    print("stop..")
print(sum)  # 打印sum最终结果
```

range函数用法

```python
range(101)         #  产生0到100范围的整数,需要注意的是取不到101.
range(1, 101)      #  产生1到100范围的整数,相当于前面是闭区间后面是开区间.
range(1, 101, 2)   #  产生1到100的奇数,其中2是步长,即每次数值递增的值.
range(100, 0, -2)  #  产生100到1的偶数,其中-2是步长,即每次数字递减的值
```





### while循环

可以在while循环后面加else语句块, 在条件为假时执行.

```python
sum = 0
a = 10
while a > 0 :
    print('OK --> ' + str(a))
    sum+=a
    a-=2
else:
    print("No..")
print(sum)
```





### break

结束当前整个循环.

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



### 函数分类

- 内建函数, 如基础函数print, 高阶函数map等.
- 用户自定义函数, 通过def, lambda关键字构造的函数.
- 第三方工具包中的函数.



### 函数定义

函数可以同时返回多个值, 实际上就是返回一个元组tuple.

```python
def function(param):
    '''说明文档,help函数可打印'''
    #函数体
	return 

# 调用
function(param)

# 打印说明文档
help(function)     # 说明文档,help函数可打印
```

**空函数定义**

```python
def nop():
    pass  # 占位符,什么都不做,避免代码报错
```



### 函数参数

参数的位置顺序必须是：`def func(必备参数, 关键字参数, 默认参数, 不定长参数)`

**形参**: 形式参数, 没有实体, 用来接受调用函数时传入的实参.

- **必备参数**: 参数以正确顺序和数量传入函数.
- **关键字参数**: 函数调用时使用等号赋值的形式传入参数
- **默认参数**: 调用函数不传任何参数时,则使用默认值.
- **不定长参数**: 函数能处理比当初声明时更多的参数.
  - `*args`是存放所有未命名的可变参数, 故接收的是元组.
  - `**kwargs`是存放关键字参数, 即形如key=value的参数, 故接收的是字典.

**实参**: 实际参数, 在调用函数时传入的数据.

```python
# 必备参数: 参数以正确顺序和数量传入函数.
def add (a,b):
    ''' 求a与b的和 '''
    return a + b 
add(1,2)

# 关键字参数: 函数调用时使用等号赋值的形式传入参数
add(a = 1,b = 2)

# 默认参数: 调用函数不传任何参数时,则使用默认值
def add (a = 1,b = 2):
    pass
add()     # 3

# 不定长参数:
# 1.存放所有未命名的可变参数,接收的是元组
def add(*args):
    pass
add(1,2,3)
# 2.存放关键字参数,接收的是字典
def add(*kwargs):
    pass
add(a = 1,b = 2,c = 3)
```



### 函数重名

由于Python没有函数重载, 所以每个文件就代表了一个模块(module), 在不同的模块中可有同名函数, 通过import导入指定的模块就可以使用同名函数.

```python
# module1.py
def foo():
 print('hello, world!')

# module2.py
def foo():
print('goodbye, world!')


# 调用
from module1 import foo
foo() # 输出hello, world!

from module2 import foo
foo() # 输出goodbye, world!
```



### 变量重名

- 全局变量: 定义在脚本中的变量.
- 局部变量: 定义在函数, 类内部的变量.

 如果变量重名, 在函数内部优先使用局部变量.

当函数中要使用的变量是全局变量时, 可以通过关键字`global`使用.

```python
name = "kk"
def func():
    # global name 引用全局变量
    name = "mm"
    print("局部变量是: %s" %name)
    
func()
print("全局变量是: %s" %name)
```



### 匿名函数

使用`lambda`关键字来创建匿名函数, 格式为 `lambda 参数: 函数体` 

```python
# lambda创建匿名函数
func = lambda x:x+1

# 调用
func(2)

# 输出x的2次方,3次方
x = 3
l = [lambda x:x**2 , lambda x:x**3]
for i in l:
    print(i(x))
```



### 高阶函数

变量可以指向函数,函数参数能接受变量,那么一个函数就可以接受另一个函数作为参数,这种函数就是高阶函数.

```python
# 函数本身也可以赋值给变量,即变量可以指向函数
f = abs
f(-10)     # 10

# 自定义高阶函数
def add(x,y,f):
    return f(x) + f(y)
print(add(1,-2,abs))     # 3
```



#### map函数

将传入的函数依次作用到每个元素,并返回新的iterator

```python
def f(x):
    return x*x
a = [1,2,3,4,5]
m=map(f,a)
list(m)     # [1, 4, 9, 16, 25]
```



#### reduce函数

把计算结果继续与下个元素做累积计算

```python
from functools import reduce
def fn(x,y):
    return x * 10 + y
a = [1,3,7,9]
reduce(fn,a)     # 1379
```



#### filter函数

传入的函数依次作用到每个元素,根据返回值为true就输出该元素.

```python
# 过滤空字符串
def not_empty(s):
    return s and s.strip()
list(filter(not_empty,['A',' ','B',None,'C']))     # ['A', 'B', 'C']
```



#### sorted函数

对可迭代的对象进行排序操作,通过key函数来实现自定义排序

```python
a = [-1,-2,0,-3,4,5]
sorted(a,key = lambda x:x+1,reverse = True)     # [5, 4, 0, -1, -2, -3]
```





## 类与对象



### 类定义

**类**: 作为设计蓝图来创建对象的代码段.

**对象**: 是类的一个实例, 通过类的构造函数创建.

```python
class 类目(父类):      # 父类可以很多个,默认继承object
     """说明文档"""
     # 类体
```



### 反射获取对象信息

```python
class Dog(object):
    
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def eat(self, food):
        print("%s 吃%s" % (self.name, food))


if __name__ == '__main__':

    dog = Dog(3, "大黄")

    # 查看对象类型
    print(type(dog))               # <class '__main__.Dog'>
    # 判断对象是否为给定的类型
    print(isinstance(dog, Dog))    # True
    # 获得对象的所有属性和方法
    print(dir(dog))                # ['__add__', '__class__', '__contains__', ...]

    # 判断对象是否有name_str的属性或者方法
    if hasattr(dog, "eat"):
        # 获取对象中与name_str同名的方法或者函数
        eat = getattr(dog, "eat")
        food = "骨头"
        eat(food)
        # 为对象设置一个以name_str为名的value方法或者属性
        setattr(dog, "temp", "饱")
        print("大黄吃%s 了" % dog.temp)
```





### 继承与多态

```python
class Animal(object):
    def run(self):
        print("runing...")

        
# 继承的体现,重写父类的方法 
class cat(Animal):
    def run(self):
        print("%s runing..." % __class__.__name__)
        
        
def run_twice(animal_name):
    animal_name.run()

    
if __name__ == '__main__':
    c = cat()
    c.run()    # cat runing...

    # 多态的体现 
    run_twice(Animal())    # runing...
    run_twice(c)           # cat runing...
```



### 私有化

**模块私有化**: 在属性或方法前加一个下划线`_`, 只能在本模块中使用, 作用是禁止import导入使用.

**完全私有化**: 在属性或方法前加双下划线`__`, 就是私有变量或方法(类似private), 作用是避免与子类中的属性命名冲突.

```python
class Student(object):
    
    '''
    属性名如果以__开头,就是私有变量(类似private),主要作用是避免与子类中的属性命名冲突
    只能内部可以访问,外部也可以使用(对象._类名__变量名)方式调用
    '''
    
    # 类的私有变量,
    __addr = "china"

    def __init__(self, name, age):
        # 实例的私有变量
        self.__name = name
        self.__age = age

    # 类似toString方法
    def __repr__(self, addr=__addr) -> str:
        return "name: %s , age : %s , addr :%s" % (self.__name, self.__age, addr)

    
    '''
    若要外部访问和修改私有属性,可以配合使用[@property,@属性.setter,@属性.getter],类似Java的get/set方法
    '''
    
    # @property: 让方法向属性一样调用
    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    # @age.setter: 设置私有属性
    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
            return self.__age
        else:
            self.__age = 18
            return self.__age

    # @age.getter: 访问私有属性
    @age.getter
    def age(self):
        return self.__age


if __name__ == '__main__':
    s = Student("kk", 25)
    print(str(s))  # name: kk , age : 25 , addr :china
    print(s._Student__name)  # kk
    print(s.name)  # kk
    s.age = 10
    print(s.age)  # 10
```





### 函数与方法

**函数**: 可直接调用, 不属于某个类的函数.

**方法**: 通过`对象.方法名`调用, 属于某个类的函数.

- **实例方法**: 第一个参数为self, 调用时该方法的对象赋值给self.
- **类方法**: 通过`@classmethod`实现, 第一个参数cls, 调用时需该方法的类赋值给cls.
- **静态方法**: 通过`@staticmethod`实现, 由`类.方法名`调用.

```python
class Persion(object):
    num = 0

    # 实例方法
    def __init__(self):
        Persion.num += 1

    # 类方法
    @classmethod
    def get_no_of_instance(cls):
        return cls.num

    # 静态方法
    @staticmethod
    def func():
        return "这是一个静态方法"


if __name__ == '__main__':
    p1 = Persion()
    p2 = Persion()
    print(p1.get_no_of_instance())  # 2
    print(p1.num)  # 2
    print(p2.num)  # 2
    print(Persion.func())  # 直接类调用  ==>  这是一个静态方法
```





### 魔法方法

**魔法方法**: 指的是python内置的,被双下划线所包围的方法; Python中一般不会被直接显示调用, 而是通过类的其他行为隐式调用的一类特殊方法.



#### new方法 / init方法

> 一般使用init方法较多.

```python
class Student(object):

    # 类级别的静态方法,创建实例时首先调用的方法,至少传递1个参数cls
    # 返回值必须是实例化出来的实例,即返回super(当前类名,cls).__new__(cls)
    # 一般用于单例模式,一旦重写该方法,就要和init方法声明的参数一致
    def __new__(cls, name, age) -> Any:
        return super(Student, cls).__new__(cls)

    # def __new__(cls) -> Any:
    #     """
    #     重写new方法,实例化对象取决于new方法返回什么就是什么
    #     """
    #     return "abc"
   
    
    # 实例级别的对象初始化方法,类似构造函数,new方法返回对象后,调用init方法进行属性的初始化
    # 第1个参数必须是self,表示new方法返回的实例本身
    # 若new方法没有返回当前类的cls实例,那init方法将不会被调用
    # 在创建实例时,必须传入与init方法声明的参数,self除外
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def print_meg(self):
        print("name: %s , age : %s" % (self.name, self.age))
        
        
if __name__ == '__main__':
    s = Student("kk", 25)
    print(s)     # <__main__.Student object at 0x000002AE0DB69670>  /  abc
    s.print_meg()
```



#### str方法 / repr方法

> 一般使用repr方法较多.

```python
class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        
    # 定义当被str()调用或者print()时的操作
    # 可重写该方法,类似Java的toString方法,返回指定格式进行显示
    def __str__(self) -> str:
        return "str方法 ==> name: %s , age : %s" % (self.__name, self.__age)

    
    # 定义当被repr()调用或者print()时的操作
    # 可重写该方法,类似Java的toString方法,返回指定格式进行显示
    # 当类中没有str方法时,会调用repr方法,所以一般类中需要定义repr方法
    def __repr__(self) -> str:
        return "repr方法 ==> name: %s , age : %s" % (self.__name, self.__age)


if __name__ == '__main__':
    s = Student("kk", 25)
    print(s)            # str方法 ==> name: kk , age : 25
    print(str(s))       # str方法 ==> name: kk , age : 25
    print(repr(s))      # repr方法 ==> name: kk , age : 25

```



#### getattr方法 / setattr方法 / getattribute方法

> getattr方法作用于访问不存在属性时, 返回自定义异常信息等.
>
> setattr方法用于属性设置值时的提示操作等.
>
> getattribute方法用于查看权限、打印log日志等.

```python
class Student(object):
    
	# 类属性
    country = "china"

    def __init__(self, name, age):
        self.name = name
        self.age = age
   

    # 定义当用户访问一个不存在的属性时的操作
    # 一般访问不存在属性时会抛出异常,重写该方法对异常进行自定义提示
    def __getattr__(self, name):
        print("获取不到该属性")
        return "Can't find the attribute ..."

    
    # 定义当一个属性被设置值时的操作
    # 在实例化调用init方法给对象初始化赋值时,也会调用该方法
    def __setattr__(self, name: str, value: Any) -> None:
        print("对 %s 设置属性值为 %s" % (name, value))
        # 重写方法时必须有其一种方式,避免无限递归情况,也可以使用 self.__dict__[name] = value
        super().__setattr__(name, value)

        
    # 属性访问拦截器,定义当该类的属性被访问时的行为
    # 每次访问属性时都会被调用1次,若直接用(类名.类属性)形式调用类属性,是不会调用该方法
    # 一般用于查看权限、打印log日志等
    def __getattribute__(self, name: str) -> Any:
        print("开启属性访问拦截器..")
        if name == "name":
            print("开始调用name属性")
        elif name == "age":
            print("开始调用age属性")
        else:
            print("开始调用其他属性")
        # 重写方法时必须返回相应的属性,避免无限递归和调用属性失败的情况
        return super().__getattribute__(name)


if __name__ == '__main__':
    s = Student("kk", 25)    # 对 _Student__name 设置属性值为 kk  /  对 age 设置属性值为 25
    print(s)                 # name: kk , age : 25
    print(s.age)             # 开启属性访问拦截器..  /  开始调用age属性  /  25
    s.age = 100        		 # 对 age 设置属性值为 100
    print(s.age) 			 # 开启属性访问拦截器..  /  开始调用age属性  /  100
    print(s.addr)		     # 开启属性访问拦截器..  /  开始调用其他属性  /  Can't find the attribute ...
    print(Student.country)   # china
```



#### del方法 / delattr方法

> 尽量不要使用del方法

```python
class Student(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    # 析构方法,定义当被del(对象)调用时的操作,销毁对象并释放其空间,程序结束时会自动调用该方法
    # 手动调用时,只有当对象引用为0的时候才会被调用,否则del(对象)删除的是对象的引用
    # 自定义del方法的实例无法被Python循环垃圾收集器收集,所以尽量不要自定义重写del方法
    def __del__(self):
        print("销毁对象 : %s" % self)

        
    # 删除属性的方法,定义当被del(属性)调用时的操作
    def __delattr__(self, name: str) -> None:
        print("删除%s属性" % name)
        # 重写方法时必须带有,避免无限递归
        super().__delattr__(name)

        
if __name__ == '__main__':
    s = Student("kk", 25)
    t = s
    print(s)  # <__main__.Student object at 0x0000021A1F38C670>
    print(t)  # <__main__.Student object at 0x0000021A1F38C670>
    print(s.age)  # name: kk , age : 25
    del (s.age)  # 删除age属性
    print(s.age)  # Can't find the attribute ...
    del (t)  # 删除对象的引用,没有调用__del__方法
    del (s)  # 对象引用为0时调用__del__方法  ==>  销毁对象 : <__main__.Student object at 0x00000215107FC670>
    '''
    程序执行完毕后,也会自动调用__del__方法,销毁s的实例化对象
    销毁对象 : <__main__.Student object at 0x000002CEC612C280>
    '''        
```





#### len方法 / bool方法

```python
class Student(object):

    def __init__(self, *args):
        self.__name = args[0]
        self.__age = args[1]
        self.number = args

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
        
        
    # 定义当被len(对象)调用时的操作,获取实例对象传入参数的个数,返回值为int类型
    # 若有私有属性,最好定义__len__方法
    def __len__(self):
        print("获取 %s 类传入参数的个数" % __class__.__name__)
        return len(self.number)

    
    # 定义当被bool(对象)调用时的操作,返回值为True/False
    # 当该对象参与任何真值判断时,都会先调用该方法,但除了bool(对象.属性)方式外
    def __bool__(self):
        print("判断age是否大于18岁")
        return True if self.__age > 18 else False


if __name__ == '__main__':
    s = Student("kk", 22, "china")
    print(len(s))  # 获取类的传入参数个数  ==>  3
    print(len(s.get_name()))  # 获取该元素的字符长度  ==>  2
    print(bool(s))  # 判断age是否大于18岁  /  True
    if s: print("oooo")  # 判断age是否大于18岁
```



### 魔法属性

**魔法方法**: 指的是python内置的,被双下划线所包围的属性.

```python
class Persion(object):
    """ 说明文档 """
    pass


if __name__ == '__main__':
    # 类的所有属性(返回字典,由类的数据属性组成)
    print(Persion.__dict__)
    """{'__module__': '__main__', '__doc__': ' 说明文档 ', 
    '__dict__': <attribute '__dict__' of 'Persion' objects>, '__weakref__': <attribute '__weakref__' of 'Persion' objects>}
    """
    # 类的说明文档
    print(Persion.__doc__)  # 说明文档

    # 类名
    print(Persion.__name__)  # Persion

    # 类定义所在的模块
    print(Persion.__module__)  # __main__

    # 类的父类(返回由所有父类组成的元组)
    print(Persion.__bases__)  # (<class 'object'>,)
```





### 单例对象

**单例模式(Singleton Pattern)**是一种常用的软件设计模式, 该模式的主要目的是**确保某一个类只有一个实例存在**.

单例模式就是创建单列对象, 重写object类里面的new方法使之开辟一个内存空间, 所有对象都指向同一内存空间, 使多个对象的引用地址相同; Python的模块导入就是天然的单例模式.

```python
class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        # 如果类属性__instance 的值为None,那么就创建一个对象,并且赋值为这个对象的引用
        # 保证下次调用这个方法时,能够知道之前已经创建过对象了,这样就保证了只有1个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


if __name__ == '__main__':
    p1 = Singleton(22, "kk")
    p2 = Singleton(52, "gg")
    print(p1)  # <__main__.Singleton object at 0x000002D13E080700>
    print(p2)  # <__main__.Singleton object at 0x000002D13E080700>
    print(p1 == p2)  # True
    print(p1 is p2)  # True
```





### 建类模板

```python
# -*- coding: utf-8 -*- 
# @Time : 2021/8/5 18:25
# @Author : koray
# @File :  建类模板


class Testmd(object):

    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def __repr__(self) -> str:
        return "name : %s , age : %s" % (self.__name, self.__age)

    def __getattr__(self, name):
        return "Can't find the attribute ..."

    @property
    def age(self):
        return self.__age

    # 设置属性
    @age.setter
    def age(self, age):
        self.__age = age
        return self.__age

    @age.getter
    def age(self):
        return self.__age


if __name__ == '__main__':
    pass
```











## 模块

在python中, 一个py文件就是一个模块, 是最高级别的组织单元.

包是一个目录, 由多个模块组成, 其中必须包含__init__.py文件.

> pyproject
> 	|
> 	|—— __init__.py
> 	|—— module0..py
> 	|—— Package_a
>            |
>            |—— __init__.py
>            |—— module0..py





### 常用内置工具包

#### os模块

> 负责与操作系统的模块

```python
# os是负责与操作系统的模块
import os

# 获取当前进程 id
print("当前进程的 ID：", os.getpid())  # 当前进程的 ID： 9404
# 获取当前父进程 id
print("当前父进程的 ID：", os.getppid())  # 当前父进程的 ID： 6904
# 获取当前所在路径
print("当前所在路径为：", os.getcwd())  # 当前所在路径为： D:\Code_Repository\python_study\list\new_kn
# 改变当前工作目录,相当于复制文件
os.chdir("./home/")
print("修改后当前所在路径为：", os.getcwd())  # 修改后当前所在路径为： ./home/
# 返回当前目录下的所有文件
print("当前目录下的文件有：", os.listdir(os.getcwd()))  # 当前目录下的文件有： ['class_kn.py', 'create_class_module.py', 'tool.py']
# 返回当前路径下的所有文件,包括子目录文件;
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
        
        
''' ==================== 文件操作 ==================== '''
# 获取当前工作目录的名称：
print(os.curdir)
# 父目录字符串名称
print(os.pardir)
# 删除指定文件
os.remove("../kn/abc.py")
# 删除文件夹
os.removedirs("./a")
# 重命名文件, rename(命名前, 命名后)
os.rename("../kn/abc.py", "../kn/1.py")


''' ==================== os.path子模块 ==================== '''
# 返回绝对路径
os.path.abspath("path")
# 文件存在则返回 True,不存在返回 False
os.path.exists("path")
# 返回文件大小, 如果文件不存在就返回错误
os.path.getsize("path")
# 判断路径是否为文件
os.path.isfile("path")
# 判断路径是否为文件夹
os.path.isdir("path")
# 拼接路径
os.path.join("path", "path2")
```



#### sys模块

> 负责与解释器交互的模块

```python
# sys是负责与解释器交互的模块
import sys

# 当前程序退出,0表示正常退出,其他值表示异常退出
sys.exit(0)
# 获取模块导入的搜索路径
l = sys.path  # 返回是list
l.append("./Code_Repository/start")  # 添加模块导入的搜索路径
print(sys.path)
# 获取当前系统平台
print(sys.platform)  # win32
# 从程序外部向程序传递参数,参数以列表的形式传递,第一个为当前文件名
print(sys.argv[0])  # D:/Code_Repository/python_study/list/new_kn/tool.py
# 获取当前版本
print(sys.version)  # 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]
# 获取当前编码
print(sys.getdefaultencoding())  # utf-8
```



#### time模块

> 处理时间的模块

```python
# time是处理时间的模块
import time

# 获取当前时间戳
print("时间戳：", time.time())  # 时间戳： 1628245640.3183932
# 获取当前时间的时间元组
localtime = time.localtime()
print("本地时间为 :", localtime)
''' 本地时间为 : time.struct_time(tm_year=2021, tm_mon=8, tm_mday=6, 
            tm_hour=18, tm_min=27, tm_sec=20, tm_wday=4, tm_yday=218, tm_isdst=0) '''
# 获取格式化的时间
print("本地时间为 :", time.asctime(localtime))  # 本地时间为 : Fri Aug  6 18:27:20 2021
# 接收当前时间的时间元组,并返回以可读字符串表示的当地时间,格式由参数format决定
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 2021-08-06 18:27:20
```



#### random模块

> 提供随机函数的模块

```python
# randmo是提供随机函数的模块
import random

# 产生1到10的一个整数型随机数
print(random.randint(1, 10))
# 产生0到1 之间的随机浮点数
print(random.random())
# 产生1.1到 5.4之间的随机浮点数,区间可以不是整数
print(random.uniform(1.1, 5.4))
# 从序列中随机选取一个元素
print(random.choice('tomorrow'))
# 生成从1到100的间隔为2的随机整数
print(random.randrange(1, 100, 2))
# 取三个值
print(random.sample("python", 3))
# 洗牌, 打乱序列
n = [1, 2, 3, 4]
random.shuffle(n)
print(n)  # [1, 4, 2, 3]
```







### 文件读写操作

#### 读取文本文件

```python
'''
book.txt:
1234567890
qwertyuiop
asdfghjkl
zxcvbnm
1234567
2wsx3edc
'''


''' ==================== r模式读取 ==================== '''
# 读取模式
f = open('book.txt', 'r', encoding="utf8")
# 读取全部内容
print(f.read())
# 返回文件中的制定大小的内容
print(f.read(10))  # 1234567890
# # 一次只读一行
print(f.readline())  # 1234567890
# # 按行读取所有,返回列表,每一项为一个f.readline()
print(f.readlines())  # ['qwertyuiop\n', 'asdfghjkl\n', 'zxcvbnm\n', '1234567\n', '2wsx3edc']
# # 返回当前文件读取位置
print(f.tell())  # 61
f.close()


''' ==================== w/a模式写入 ==================== '''
# 覆盖写入
# overwrite = open('book.txt', 'w', encoding="utf8")
# 追加写入
update = open('book.txt', 'a', encoding="utf8")
# 写入字符串数据
update.write("\twrite... \n")
# 定位文件读写位置,off表示偏移量,where为0表示起始位置开始,1表示当前位置,2表示结尾位置
print(update.seek(3, 0))
# 将缓存内容写入硬盘
update.flush()
# 关闭文件
update.close()


''' ==================== with: 上下文管理器 ==================== '''
# with: 上下文管理器,自动关闭文件,不需要调用close
with open('book.txt', 'r', encoding="utf8") as r:
    print(r.read())
```



#### 读取图片文件

可以使用openCV, skimage, pillow等工具包实现图片文件的读写功能.

```python
''' ==================== open模块读取图片 ==================== '''
# open模块读取文本以外的文件,读取模式是rb的二进制读取方式,返回二进制数据
# bytes类型是指一堆字节的集合,在python中以b开头的字符串都是bytes类型
with open('a.png', 'rb') as pr:
    print(pr.read())  # 二进制数据  ==>  b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00

    
''' ==================== cv2模块读取图片的像素矩阵 ==================== '''
# cv2模块获取图片的像素矩阵
# 安装cv2库 : pip install opencv-python
import cv2

img = cv2.imread('a.png')
print(img)
'''
[[[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [255 255 255]
  [255 255 255]]
'''
```



#### 读取音频文件

可以使用wave, scipy, pyaudio等工具包实现音频文件的读写功能.

```python
''' ==================== open模块读取音频文件 ==================== '''
# open模块读取文本以外的文件,读取模式是rb的二进制读取方式,返回二进制数据
with open("music.wav", "rb") as f:
    print(f.read())  # b'\x00\x00\x00\x18ftypmp42\x00\x00\x00


''' ==================== wavfile模块读取音频的矩阵 ==================== '''
# 获取音频的矩阵
from scipy.io import wavfile

wav = wavfile.read("music.wav")
# print(wav)
'''
(48000, array([[   0,    0],
       [   0,    0],
       [   0,    0],
       ...,
       [-116, -116],
       [-116, -116],
       [-114, -114]], dtype=int16))
'''
```



#### 读取csv文件

> 1. csv文件有表头并且是第一行, 那么names和header都无需指定;
> 2. csv文件有表头, 但表头不是第一行, 需要指定header,参数从0开始;
> 3. csv文件有表头, 但想自定义表头, 同时使用names和header即可;
> 4. csv文件没有表头且纯数据, 使用names生成表头;

```python
'''
test.csv :
a	b	c	d	e
1	kk	25	china	2021年08月07日
2	gg	22	guangzhou	2021年08月07日
3	zz	18	fujian	2021年08月07日
3	zz	183224	fujian	2021年08月07日
3	zz	184234234234	fujian	2021年08月07日
3	zz	18243243	fujian	2021年08月07日
'''

import pandas as pd
from datetime import datetime
csv = pd.read_csv("test.csv", encoding="GBK",
                  sep="\t",  # 分隔符
                  names=["编号", "名字", "年龄", "地址", "日期"],  # 生成表头
                  header=0,  # 指定表头列
                  usecols=["编号", "名字", "年龄", "日期"],  # 只获取指定的列
                  index_col="编号",  # 指定索引列

                  # ================ 不常用操作 =======================
                  dtype={"编号": str},  # 指定列的类型
                  converters={"年龄": lambda x: int(x) + 10},  # 读取文件时,对指定列进行数据处理操作
                  nrows=1,  # 一次性读取文件的行数,常用于看大文件的字段内容
                  na_values={"名字": "kk", "日期": datetime},  # 指定某列的某内容为NaN
                  verbose="true",  # 打印额外信息

                  # ================ 日期处理 =======================
                  parse_dates=["日期"],  # 指定某列为时间类型,配合date_parser使用
                  date_parser=lambda x: datetime.strptime(x, "%Y年%m月%d日"),  # 解析日期格式
                  infer_datetime_format="true"  # 设置为true,date_parser的解析性能提高
                  )

print(csv)
```





### 常用小技巧

```python
''' =========== 1.变量值互换与多元赋值 ==================== '''
a = 3
b = 2
a, b = b, a
c, d = 8, 9


''' =========== 2.三元表达式(true if 条件 else false),比较2个数字的大小 ==================== '''
a = 8
b = 9
print(a if a > b else b)


''' =========== 3.推导式生成数据 ==================== '''
# 列表
List = [i ** 2 for i in range(-5, 5) if i % 2]  # [25, 9, 1, 1, 9]
# 集合
Set = {i ** 2 for i in range(-5, 5) if i % 2}  # {25, 9, 1}
# 字典
Dict = {x: y for x, y in zip(["a", "b"], (1, 2))}  # {'a': 1, 'b': 2}


''' =========== 4.小整数对象池 ==================== '''
# python为了优化速度,使用[-5,256]范围的小整数对象池,避免了整数频繁申请和销毁内存空间,这些整数对象会提前建立好,不会被回收.
a = 0
b = 0
print(id(a) == id(b))  # True

# 当字符串中不存在空格和特殊字符时,也有一样的优化
i = "kk"
l = "kk"
print(i is l)  # True


''' =========== 5.数据解包 ==================== '''
# 数据解包
# 需求:获取一个列表中的数据
# 1.for循环
for i in [1, 2, 3]:
    print(i)
# 2.使用相同数量的变量接收
a, b, c = [1, 2, 3]
# 3.使用星号*解包
L = [1, 3, 3]
print(*L)  # 1 3 3
```





## 异常与调试



### 异常

#### 异常处理

```python
try:
    num = 0
    result = 1 / num
except Exception:
    print("num不能为0")
finally:
    print("程序结束..")
```



#### 自定义异常

1. 通过继承类Exceptio来实现自定义的异常
2. 使用raise抛出自定义异常

```python
# 1.通过继承类Exceptio来实现自定义的异常
class MyException(Exception):

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


def func(age):
    if 100 > age > 18:
        return 1
    else:
        # 2.使用raise抛出自定义异常
        raise MyException("未成年不准进入网吧")
    

if __name__ == '__main__':
    func(16)  # __main__.MyException: 未成年不准进入网吧
```





### 调试

#### assert断点

assert是python中用于调试的工具.

- 格式 :  `assert (expression..), "抛出错误的自定义信息"`

- 在运行带有assert语句的脚本时, 可通过`-O`参数来屏蔽assert.

```python
def foo(num):
    assert type(num) == int, "num 必须为整形"
    assert num != 0, 'n is zero!'
    return 10 / num
foo(0)
'''
Traceback (most recent call last):
  File "E:/python_study/list/new_kn/test.py", line 39, in <module>
    foo(0)
  File "E:/python_study/list/new_kn/test.py", line 37, in foo
    assert num != 0, 'n is zero!'
AssertionError: n is zero!
'''
```



#### unittest单元测试

unittest是python内置的单元测试框架.

> myPY.py文件

```python
import re

class CheckUserInfo():
    def check_pwd_len(self, pwd):
        """密码长度不超过 8 位"""
        return len(pwd) >= 8

    def check_pwd_contain_leter(self, pwd):
        """密码包含大小写英文字母"""
        flag = False
        pattern = re.compile('[A-Z][a-z]+')
        match = pattern.findall(pwd)
        if match:
            flag = True
        return flag
```

> 测试用例

```python
from myPY import CheckUserInfo
import unittest

# 需要继承unittest.TestCase类创建测试用例类
class CheckUserInfoTestCase(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.check_user_info = CheckUserInfo()

    # 在所有测试方法执行之前执行
    @classmethod
    def setUpClass(cls):
        print('setUpClass\n\n')

    # 在所有测试方法执行之后执行
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # 在每个测试方法执行之前执行
    def setUp(self):
        print('setUp')

    # 在每个测试方法执行之后执行
    def tearDown(self):
        print('tearDown\n')

        
    # 以test开头的方法,都会独立执行
    def test_check_pwd_len(self):
        print('test_check_pwd_len')
        self.assertEqual(True, self.check_user_info.check_pwd_len('12345678'))
        self.assertEqual(False, self.check_user_info.check_pwd_len(''))
        self.assertEqual(False, self.check_user_info.check_pwd_len('1'))
        self.assertEqual(True, self.check_user_info.check_pwd_len('123456789'))

    def test_check_pwd_contain_letter(self):
        print('test_check_pwd_contain_leter')
        self.assertEqual(True, self.check_user_info.check_pwd_contain_leter('1qazXSW@'))
        self.assertEqual(False, self.check_user_info.check_pwd_contain_leter('12345678'))
        self.assertEqual(False, self.check_user_info.check_pwd_contain_leter(''))

    def aaa(self):
        print('test_check_pwd_contain_num')
        self.assertEqual(True, self.check_user_info.check_pwd_contain_num('1qazXSW@'))


if __name__ == '__main__':
    # 执行测试用例
    unittest.main()

"""
setUpClass
setUp
test_check_pwd_contain_leter
tearDown
FsetUp
test_check_pwd_len
tearDown
.tearDownClass
======================================================================
FAIL: test_check_pwd_contain_letter (__main__.CheckUserInfoTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "mytest.py", line 33, in test_check_pwd_contain_letter
    self.assertEqual(True, self.check_user_info.check_pwd_contain_leter('1qazXSW@'))
AssertionError: True != False
----------------------------------------------------------------------
Ran 2 tests in 0.001s
FAILED (failures=1)
"""
```





## 3个神器



### 迭代器



#### 可迭代对象

可迭代对象, 能被for循环遍历的对象.

```python
# 1.使用for循环遍历判断
List = [1, 2, 3]
str_ = "py3"
Tuple = (9, 8, 7)
Dict = {"a": 1, "b": 2, "c": 3}
Set = {"A", "B", "C"}
for i in zip(List, str_, Tuple, Dict, Set):
    print(i)

    
# 2.使用Iterable方法判断
from collections.abc import Iterable
print("list:", isinstance(List, Iterable))  # True
print("str:", isinstance(str_, Iterable))  # True
print("tuple:", isinstance(Tuple, Iterable))  # True
print("dict:", isinstance(Dict, Iterable))  # True
print("set:", isinstance(Set, Iterable))  # True
print("num:", isinstance(1, Iterable))  # False
```



#### 自定义可迭代对象

实现`__iter__`和`__getitem__`方法.

```python
class Iter_obj(object):
    def __init__(self, value):
        self.value = value

    # 编写迭代逻辑
    def __iter__(self):
        self.index = 3
        return iter(self.value[:self.index])


L = Iter_obj([1, 2, 3, 4, 5, 6])
print(isinstance(L, Iterable))  # True
for i in L:
    print(i)  # 只打印到索引为3,因为__iter__限制
```



#### 迭代器对象

- 可迭代对象不是迭代器, 但是迭代器是可迭代对象.
- 迭代器在循环遍历中是不可逆的.

```python
# 使用Iterable方法判断是否迭代器对象
from collections.abc import Iterator
print("list:", isinstance(List, Iterator))      # False
print("str:", isinstance(str_, Iterator))       # False
print("tuple:", isinstance(Tuple, Iterator))  	# False
print("dict:", isinstance(Dict, Iterator))  	# False
print("set:", isinstance(Set, Iterator))  	  	# False
print("num:", isinstance(1, Iterator)) 		 	# False


# 使用iter()方法将可迭代对象转换为迭代器对象,且迭代器在循环遍历中是不可逆的.
l = iter([1, 2])
print(isinstance(l, Iterator))  # True
next(l)  # 1
next(l)  # 2
next(l)  # StopIteration
```





#### 自定义迭代器对象

实现`__iter__`和`__next__`方法;  其中`__iter__`方法放回迭代器对象本身, next()方法返回容器的下一个元素,在没有后续元素时抛出StopIteration异常.

```python
class IterObj(object):
    def __init__(self, value):
        self.value = value
        self.i = 0

    def __iter__(self):
        return iter(self.value)

    # 编写迭代逻辑
    def __next__(self):
        while self.i < len(self.value):
            v = self.value[self.i]
            self.i += 1
            return v
        # 此处可以增加StopIteration异常提示
        print("StopIteration...")


ite = IterObj([1, 2, 3, 4, 5])
print(isinstance(ite, Iterable))  # True
next(ite)
```





### 生成器

生成器generator, 是一类特殊的迭代器, 性能上比迭代器好.

生成器可使用next和send取值,

- next, 获取下一个元素.
- send, 获取下一个元素, 同时可以向生成器重传递一个值.
- 第一次取值时, 必须使用next或者send(None).

```python
# 1.推导式创建生成器,元组不具备推导式生成,故创建的都是生成器对象
g = (x * 2 for x in range(5))
next(g)
g.send("取值成功")


# 2.使用yield创建生成器,每次会在yield的地方暂停并重新进入while,直到循环完毕了才执行return
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1 + num2
        current += 1
        yield num
    return 'done'

g = fib(5)

while True:
    try:
        x = next(g)
        print("value:%d" % x)
    except StopIteration as e:
        print("生成器返回值:%s" % e.value)
        break
'''
value:0
value:1
value:1
value:2
value:3
生成器返回值:done
'''
```





### 装饰器



#### 闭包

- 在一个内部函数中, 对外部作用域的变量进行引用, 且一般外部函数的返回值为内部函数, 那么内部函数就被认为是闭包.
- 闭包中不可以直接修改外部函数的局部变量(可变类型除外), 需使用关键字`nonlocal`.
- 装饰器是闭包的一种应用.

```python
''' 
在函数func中定义了一个inner函数,inner访问了外部函数func的变量,并且函数返回值为inner函数  
'''
def func(x):
    z = 0
    def inner(y):
    	z = 2
        return x + y
    print(z) # 还是0,修改不了z变量
    return inner
```





#### 装饰器创建

- 装饰器本质是一个python函数, 它可以再不改变代码结构的情况下给代码添加新的功能.
- 装饰器多用于有切面需求的场景, 比如插入日志、性能测试、事务处理、缓存、权限校验等.
- 装饰器的工作过程: 将被装饰的函数当作参数传递给装饰器函数, 并返回装饰后被装饰的函数.
- 装饰器会丢失原有函数的元信息, 可使用 `@warps` 来解决.
- 解除装饰器功能, 可使用 `函数.__wrapped__` 方法.
- 装饰器其实就是两个嵌套函数返回内部函数.

```python
# 导包
from functools import wraps


# 定义装饰器函数
def Decorator(func):
    @wraps(func)   # 防止装饰器导致元信息丢失,且有解除装饰器功能
    def inner(*args, **kwargs):  # 通用的装饰器参数
        '''装饰器功能逻辑编写...'''
        func(*args, **kwargs)
    return inner


# 定义被装饰函数
@Decorator
def func():
    pass

# 解除装饰器
func.__wrapped__()
```



#### 外参的装饰器

```python
# 定义装饰器函数
def Decorator(name=None, level="普通会员"):
    def outer(func):
        def inner(name):
            if level == "SVIP":
                print("欢迎登陆尊贵的%s用户,过期时间还有1年" % level)
                func(name)
            else:
                print("欢迎登陆, %s" % level)
                func(name)
        return inner
    return outer

# 定义被装饰函数,并外部传参
@Decorator(level="SVIP")
def func(name):
    print(name)


func("张三")
'''
欢迎登陆尊贵的SVIP用户,过期时间还有1年
张三
'''
```





#### 装饰器装饰类

典型的单例对象创建.

```python
# 单例对象装饰器逻辑
def singleton(cls, *args, **kw):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
            return instance[cls]
    return _singleton


@singleton
class Singleton(object):
    def __init__(self):
        self.num_sum = 0

    def add(self):
        self.num_sum = 100
```





#### 类装饰器创建

类方法装饰器与实例方法装饰器的调用方式不同.

```python
class Tiga(object):
    
    # 类装饰初始化参数为函数
    def __init__(self, func):
        self.func = func

    # 定义__call__方法, 让类像方法一样被调用.
    def __call__(self, *args, **kwargs):
        print("叮~, 变身")
        self.func(*args, **kwargs)
        print("光之巨人")

    # 实例方法装饰器
    def Red(self, f):
        def wrapper(*args, **kwargs):
            print("切换战士形态：力量+100")
            f(*args, **kwargs)
        return wrapper

    # 类方法装饰器
    @classmethod
    def Blue(cls, f):
        def wrapper(*args, **kwargs):
            print("切换刺客形态：敏捷+100")
            f(*args, **kwargs)
        return wrapper

    
# 类装饰器调用
@Tiga
def func():
    print("化身成为光！")

# 相当于实例化的对象 func = Tiga()
func()


# 类方法装饰器的调用格式: @类名.类方法
@Tiga.Blue
def fight1():
    print("速度很快, 但是没有破防")
fight1()


# 实例方法装饰器的调用格式: @对象.实例方法
@func.Red
def fight2():
    print("使出一记重拳, 但是没打中")
fight2()
```





#### 多装饰器使用

多个装饰器的使用, 先执行距离主函数近的装饰器, 依次类推.

```python
from functools import wraps

def a(func):
    @wraps(func)
    def a_inner():
        func()
        print("==> 执行a装饰器")
        pass
    return a_inner

def b(func):
    @wraps(func)
    def b_inner():
        func()
        print("==> 执行b装饰器")
        pass
    return b_inner

def c(func):
    @wraps(func)
    def c_inner():
        func()
        print("==> 执行c装饰器")
        pass
    return c_inner


@a
@b
@c
def P():
    print("执行P函数")
    
P()
'''
执行P函数
==> 执行c装饰器
==> 执行b装饰器
==> 执行a装饰器
'''

# 解除装饰器,使用__wrapped__方法
p_remove = P.__wrapped__.__wrapped__.__wrapped__
p_remove()
```







## 正则表达式



### re模块

re模块中通过给定的匹配规则, 匹配文本中符合规则的字符并进行操作.

```python
# 导包
import re

# 匹配以给定条件开头的字符串,失败返回none,通过调用group()方法得到匹配的字符串
re.match("www", "www.koray2021.ml").group()   # www
re.match("www", "www.koray2021.ml").span()    # 匹配到的区间下标  ==>  (0, 3)


# 扫描整个字符串并返回第一个成功的匹配,通过调用group()方法得到匹配的字符串
re.search("www", "yuiwwwyuiswww.ml")
re.search("www", "yuiwwwyuiswww.ml").group()  # www
re.search("www", "yuiwwwyuiswww.ml").span()   # (3, 6)

# 查找所有的符合条件的文本
re.findall("w", "adjawadjw79w")  			  # ['w', 'w', 'w']

# 字符串替换
re.sub(r"\d+", "101", "abc = 22")  			  # abc = 101

# 字符串切割
re.split("\.", "www.koray2021.ml")  		  # ['www', 'koray2021', 'ml']

# 编译正则表达式,获得一个正则表达式对象,即提前写好正则规则
pattem = re.compile("\.")
pattem.split("www.koray2021.ml")  			  # ['www', 'koray2021', 'ml']
pattem.search("www.koray2021.ml").group()
```



### 正则表达式模式

| 实例        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| [Pp]ython   | 匹配 "Python" 或 "python"                                    |
| rub[ye]     | 匹配 "ruby" 或 "rube"                                        |
| [aeiou]     | 匹配中括号内的任意一个字母                                   |
| [0-9]       | 匹配任何数字. 类似于 [0123456789]                            |
| [a-z]       | 匹配任何小写字母                                             |
| [A-Z]       | 匹配任何大写字母                                             |
| [a-zA-Z0-9] | 匹配任何字母及数字                                           |
| [^aeiou]    | 除了aeiou字母以外的所有字符                                  |
| [^0-9]      | 匹配除了数字外的字符                                         |
| .           | 匹配除 "\n" 之外的任何单个字符.                              |
| \d          | 匹配一个数字字符. 等价于 [0-9].                              |
| \D          | 匹配一个非数字字符. 等价于 \[^0-9].                          |
| \s          | 匹配任何空白字符, 包括空格、制表符、换页符等等. 等价于 [ \f\n\r\t\v]. |
| \S          | 匹配任何非空白字符. 等价于 \[^ \f\n\r\t\v].                  |
| \w          | 匹配包括下划线的任何单词字符. 等价于'[A-Za-z0-9_]'.          |
| \W          | 匹配任何非单词字符. 等价于 '\[^A-Za-z0-9_]'.                 |

```python
# 使用\d (小写)匹配数字
re.findall(r'\d+', "qeqw123ytu3792")  # ['123', '3792']
# 使用\D (大写)匹配任意的非数字字符
re.findall(r'\D+', "qeqw123ytu你好世界")  # ['qeqw', 'ytu你好世界']

# 使用\w (小写)匹配数字字母下划线
re.findall(r'\w+', "qeqw~.;[ps]\=|123ytuc 你好世界37adw_ee43")  # ['qeqw', 'ps', '123ytuc', '你好世界37adw_ee43']
# 使用\W (大写)匹配非数字字母下划线
re.findall(r'\W+', "qeqw~.;[ps]\=|123ytuc 你好世界37adw_ee43")  # ['~.;[', ']\\=|', ' ']

# 使用\s (小写)匹配任意空白字符
re.findall(r'\s+', "qeqw123ytu37 92_adw_ee43")
# 使用\S (大写)匹配任意非空字符
re.findall(r'\S+', "qeqw123ytu37 92_adw_ee43")  # ['qeqw123ytu37', '92_adw_ee43']

# 只匹配数字,使用[]指定匹配元素的范围, {}指定匹配次数
re.findall(r'[0-9]{1,3}', "qeqw123ytu3792")  # ['123', '379', '2']
# 只匹配英文字母
re.findall(r'[A-Za-z]+', "qeqw123ytu你好世界37 92_adw_ee43")  # ['qeqw', 'ytu', 'adw', 'ee']
# 只匹配中文, \u4e00和\u9fa5 两个unicode值正好是Unicode表中的汉字的头和尾.
re.findall(r'[\u4e00-\u9fa5]{1,}', "qeqw123ytu你好世界37 92_adw_ee43")  # ['你好世界']
```



### 贪婪模式与赖惰模式

- 尝试匹配尽可能多的字符模式就是贪婪模式

- 尝试匹配尽可能少的字符模式就是非贪婪模式, 需要在表达式的`"*","?","+","{m,n}"`后面加上`?`实现非贪婪模式.

```python
# 贪婪模式下的匹配
# 尝试匹配尽可能多的字符
html = "aa<div>test1</div>bb<div>test2</div>cc "
re.search("<div>.*</div>", html).group()  # '<div>test1</div>bb<div>test2</div>'

# 非贪婪模式下的匹配
# 尝试匹配尽可能少的字符,需要在表达式的"*","?","+","{m,n}"后面加上?实现非贪婪模式
html = "aa<div>test1</div>bb<div>test2</div>cc "
re.search("<div>.*?</div>", html).group()  # '<div>test1</div>'
```



### 正则表达式修饰符

正则表达式可以包含一些可选标志修饰符来控制匹配的模式, 修饰符被指定为一个可选的标志.

| 修饰符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| re.I   | 使匹配对大小写不敏感                                         |
| re.L   | 做本地化识别（locale-aware）匹配                             |
| re.M   | 多行匹配, 影响 ^ 和 $                                        |
| re.S   | 使 . 匹配包括换行在内的所有字符                              |
| re.U   | 根据Unicode字符集解析字符. 这个标志影响 \w, \W, \b, \B.      |
| re.X   | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解. |

```python
# re.I对大小写不敏感
s = re.match("life is short", "Life is short, you need Python", flags=re.I).group()  
print(s)  # Life is short
```



### 正则表达式常用用法

```python
# 匹配文本信息中的邮箱信息
re.findall(r'[A-Za-z0-9]+@[A-Za-z0-9]+\.com', "我的邮箱是 python996@icu.com")

# 匹配网址URL
re.findall(r'[a-zA-z]+://[^\s]*', "我的个人主页：https://www.python.org")

# 匹配身份证号码
s = re.findall(r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)', "假的身份证:12345678901234567X")
print(s)  # [('123456', '7890', '12', '34', '567', 'X')]
print("".join(s[0]))  # '12345678901234567X'

# 匹配手机号码
re.findall(r'\d{3}\d{8}|\d{4}\{7,8}', "假的手机:13012345678")

# 匹配日期格式
re.findall(r'\d{4}-\d{1,2}-\d{1,2}', "日期是2021-02-22")

# IP地址
re.findall(r'\d{3}\.\d{3}\.\d{3}\.\d{3}', "IP地址为192.168.100.140")
```





## Numpy科学计算库



### 数组模块

#### 数组创建

```python
# ====================  普通数组创建  =======================
# 创建数组
np.array([2, 5, 7])  			  	# 一维数组 ==> array([2 5 7])
np.array([[2, 5, 7], [8, 9, 0]])  	# 多维数组 ==> array([[2, 5, 7], [8, 9, 0]])

# 将数据转化为数组
a = [1, 2, 3, 4]
np.asarray(a)  						# array([1, 2, 3, 4])


# ====================  全等值数组创建  =======================
# 创建多维形状的全零数组
np.zeros([2, 2]) 				    # array([[0., 0.], [0., 0.]])

# 创建多维形状的全1数组
np.ones([2, 2])  				    # array([[1., 1.], [1., 1.]])

# 创建多维形状的全指定原元素值的数组
np.full([2, 2], 8)  				# array([[8., 8.], [8., 8.]])


# ====================  等间隔数组创建  =======================
# 生成等间隔的数组, np.arange(start, stop, step, dtype)
np.arange(0, 10, 2)  			    # array([0 2 4 6 8])

# 生成等间隔的数组
np.linspace(1, 2, num=10) 		    # array([1. 1.11111111 1.22222222 1.33333333 1.44444444 1.55555556 1.66666667 1.77777778 1.88888889 2.  ])


# ====================  特殊数组创建  =======================
# 创建多维形状的未初始化数组,打印的值是随机无意义的
np.empty([2, 2])

# 生成类似于对角矩阵的数组  np.eye(N, M=None, k=0, dtype=float, order='C')  
# [N为行数,M为列数,k为对角线的索引,0代表主对角线]
np.eye(4, 4, 0)
'''
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
'''
```





#### 数组操作

##### 获取数组属性

```python
# 数组的形状维度 (行数,列数)
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.shape)            # (3, 2)

# 获取数组的维度数
print(a.ndim)       	  # 2维数据
b = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]])
print(b.ndim)      		  # 3维数据

# 数组元素的个数
print(a.size)       	  # 6

# 改变数组维度,但是不能改变数组元素个数
print(a.reshape(2, 3))   # array([[1, 2, 3], [4, 5, 6]])

# 数组第一维度上的大小,即行数;数组第二维度上的大小,即列数;
print(a.shape[0])       # 行数  ==>  3
print(a.shape[1])       # 列数  ==>  2
print(np.size(a, 0))    # 行数  ==>  3
print(np.size(a, 1))    # 列数  ==>  2
print(len(a))           # 行数  ==>  3
```



##### 切片与索引操作

```python
# ====================  索引操作  =======================
# 数组[[第1个值的行下标,第2个值的行下标], [第1个值的列下标,第2个值的列下标]]
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
a[2]                 # array([6, 7, 8])
a[[2, 0], [0, 2]]    # array([6, 2])


# ====================  切片操作  =======================
# 数组[行操作,列操作],下标包头不包尾
a[:2, :3] 			 # array([[0, 1, 2], [3, 4, 5]])
a[2, :]   			 # array([6, 7, 8])
a[2:, :]   			 # array([[6, 7, 8]])

# slice类似设定切片规则传入
s = slice(0, 3)  
a[s]      			# array([0, 1, 2])

# 布尔运算获取值,判断每个元素是否符合条件
a[a > 4]  			# array([5, 6, 7, 8])
```



##### 数组操作函数

```python
# ====================  拼接操作  =======================
# 根据指定维度(行,列)方向进行拼接
# 默认为axis=0,即根据第1维度的行进行拼接,当axis=1,即根据第2维度的列进行拼接
a = np.arange(6).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
np.concatenate((a, b))              # 维度(4,3) ==> array([[ 0,  1,  2], [ 3,  4,  5], [ 7,  8,  9], [10, 11, 12]])
np.concatenate((a, b), axis=1)      # 维度(2,6) ==> array([[ 0,  1,  2,  7,  8,  9],  [ 3,  4,  5, 10, 11, 12]])


# ====================  堆叠操作  =======================
# 根据指定维度(行,列)方向进行堆叠数组,与concatenate不同的是会拓展维度
# 当axis=0,即根据第1维度的行进行堆叠,当axis=1,即根据第2维度的列进行堆叠
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
np.stack((a, b), 0)                 # array([[[1, 2], [5, 6]], [[3, 4], [7, 8]]])
np.stack((a, b), 1)                 # array([[[1, 2], [5, 6]], [[3, 4], [7, 8]]])


# ====================  追加操作  =======================
# 根据指定维度(行,列)方向,在数组的后面追加values,values的维度要与数组的指定维度数一致
# 当axis=0,即根据第1维度的行进行追加,当axis=1,即根据第2维度的列进行追加
a = np.arange(6).reshape(2, 3)
np.append(a, [[7, 8, 9]], axis=0)                    # array([[0, 1, 2], [3, 4, 5]])
np.append(a, [[7, 8, 9], [10, 11, 12]], axis=1)      # array([[ 0,  1,  2,  7,  8,  9], [ 3,  4,  5, 10, 11, 12]])


# ====================  插入操作  =======================
# 根据指定维度(行,列)方向,在数组的指定索引位置插入values,values的维度要与数组的指定维度数一致
# 当axis=0,即根据第1维度的行进行插入,当axis=1,即根据第2维度的列进行插入
a = np.arange(6).reshape(2, 3)
np.insert(a, 1, [[7, 8, 3], [9, 10, 3]], axis=0)     # array([[ 0,  1,  2], [ 7,  8,  3], [ 9, 10,  3], [ 3,  4,  5]])
np.insert(a, 2, [7, 8], axis=1)                      # array([[0, 1, 7, 2], [3, 4, 8, 5]])


# ====================  删除操作  =======================
# 根据指定维度(行,列)方向,在数组的指定索引位置进行删除操作
# 当axis=0,即根据第1维度的行进行删除,当axis=1,即根据第2维度的列进行删除
a = np.arange(6).reshape(2, 3)
np.delete(a, 0, axis=0)                              # array([[3, 4, 5]])
np.delete(a, 1, axis=1)                              # array([[0, 2], [3, 5]])


# ====================  转置操作  =======================
# 数组转置,调换数组的行列值的索引值
a = np.arange(12).reshape(2, 2, 3)
b = np.transpose(a, (2, 0, 1))
```





#### UFunc数学函数

ufunc是universal function缩写, 是一种能对数组的每个元素进行操作的函数.

```python
# ====================  三角函数  =======================
a = np.array([0, 30, 45, 60, 90])
np.sin(a * np.pi / 180)
np.cos(a * np.pi / 180)
np.tan(a * np.pi / 180)


# ====================  舍取操作  =======================
a = np.array([1.0, 1.5, 2.0, 2.55])
np.around(a)                    # 四舍五入  ==> array([1., 2., 2., 3.])
np.around(a, decimals=1)        # 四舍五入,保留1位小数  ==>  array([1. , 1.5, 2. , 2.6])
np.floor(a)                     # 向下取整  ==> array([1., 1., 2., 2.])
np.ceil(a)                      # 向上取整  ==> array([1., 2., 2., 3.])


# ====================  算数运算  =======================
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])
np.add(a, b)                    # 加
np.subtract(a, b)               # 减
np.multiply(a, b)               # 乘
np.divide(a, b)                 # 除
np.mod(a, b)                    # 取余
np.power(a, b)                  # 乘方


# ====================  统计操作  =======================
a = np.arange(6).reshape(2, 3)
np.amin(a, 0)                   # 最小值  ==>  array([0, 1, 2])
np.amax(a, 1)                   # 最大值  ==>  array([2, 5])
np.median(a)                    # 中位数  ==>  2.5
np.mean(a)                      # 平均数  ==>  2.5


# ====================  排序操作  =======================
a = np.array([[3, 5, 1], [2, 8, 7]])
np.sort(a, axis=0)              # 对每列的行元素进行排序  ==>  array([[2, 5, 1], [3, 8, 7]])
np.sort(a, axis=1)              # 对每行的列元素进行排序  ==>  array([[1, 3, 5], c[2, 7, 8]])
```





#### 数组广播

广播 (Boardcasting) 是NumPy中用于在不同大小的阵列之间进行逐元素运算的一组规则.

- 两个数组的shape长度相等时,对应元素逐元素运算
- 两个数组的shape长度不相等时,对应元素逐元素运算,对较小数组进行自身拓展,再与较大数组进行逐元素运算

```python
# ====================  两个数组的shape长度相等  =======================
'''两个数组的shape长度相等时,对应元素逐元素运算'''
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
print(a * b)  # array([ 1,  4,  9, 16])
print(a + 5)  # array([6, 7, 8, 9])


# ====================  两个数组的shape长度不相等  =======================
'''两个数组的shape长度不相等时,对应元素逐元素运算,对较小数组进行自身拓展,再与较大数组进行逐元素运算'''
a = np.arange(9).reshape([3, 3])
b = np.array([1, 2, 3])
print(a + b)
'''
array([[0, 1, 2],      array([[1, 2, 3]])           array([[ 1,  3,  5],
       [3, 4, 5],   +  array([[1, 2, 3]])   ====>          [ 4,  6,  8],
       [6, 7, 8]])     array([[1, 2, 3]])                  [ 7,  9, 11]])
'''
```





### 矩阵模块

#### 矩阵创建

```python
# 导包
import numpy as np
import numpy.matlib

# 创建矩阵
b = np.mat([[1, 2], [3, 4]])       # matrix([[1, 2], [3, 4]])
c = np.matrix([[1, 2], [3, 4]])    # matrix([[1, 2], [3, 4]])
d = np.asmatrix([[1, 2], [3, 4]])  # matrix([[1, 2], [3, 4]])

# 全零矩阵
np.matlib.zeros([2, 2])  	   	   # matrix([[0., 0.], [0., 0.]])

# 全一矩阵
np.matlib.ones([2, 2])  		   # matrix([[1., 1.], [1., 1.]])

# 对角矩阵
np.matlib.eye(3)  				   # matrix([[1., 0.], [0., 1.]])

# 随机生成矩阵
np.matlib.rand(2, 2)  			   # matrix([[0.15843201, 0.84915475],  [0.8656387 , 0.51666915]])
```



#### 矩阵操作

```python
# 两矩阵对应元素相乘 
a = np.mat([[1], [2], [3]])
b = np.mat([1, 2, 3])
print(a * b)                    # matrix([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
print(np.multiply(a, b))        # matrix([[1, 2, 3], [2, 4, 6], [3, 6, 9]])

# 矩阵求逆
a = np.matrix([[2, 0, 0], [0, 1, 0], [0, 0, 2]])
print(a.I)                      # matrix([[0.5, 0. , 0. ], [0. , 1. , 0. ], [0. , 0. , 0.5]])

# 矩阵转置
print(a.T)                      # matrix([[2, 0, 0], [0, 1, 0], [0, 0, 2]])

# 行列式值的计算
a = np.matrix([[1, 2], [3, 4]])
b = np.linalg.det(a)
print(b)                        # -2.0000000000000004

# 求和与最大最小
a = np.matrix([[1, 2], [3, 4]])
print(a.sum(axis=0))            # 列求和  ==>  matrix([[4, 6]])
print(a.sum(axis=1))            # 行求和  ==>  matrix([[3], [7]])
print(a.max())                  # 4
print(a.min())                  # 1

# 矩阵转数组,getA()将矩阵类转化为数组类
a = np.mat([[1, 2, 3], [4, 5, 6]])
b = a.getA()
print(b)                        # array([[1, 2, 3], [4, 5, 6]])
```



### 数组与矩阵

```python
matrices必须是2维的,arrays可以是多维
matrix是array的分支,拥有array的所有特性

如果两个可以通用, 那就选择array, 因为array更灵活, 速度更快;
arrays可以使用简单运算做元素相乘,而矩阵相乘,则需要numpy里面的dot命令

运算符的作用也不一样 ：因为a是个matrix, 所以a**2返回的是a*a, 相当于矩阵相乘. 而c是array, c**2相当于, c中的元素逐个求平方
两条命令轻松的实现两者之间的转换：np.asmatrix和np.asarray
numpy 中的array与numpy中的matrix的最大的不同是, 在做归约运算时, array的维数会发生变化, 但matrix总是保持为2维
```





### 随机数模块

#### 随机数生成

```python
# ====================  简单随机数生成  =======================
# 生成范围在[0,1)的随机数数组
np.random.rand(2)  # array([0.09167149, 0.90996157])
np.random.rand(2, 2)  # array([[0.18880545, 0.61878701], [0.54042711, 0.92894623]])

# 生成范围在[0,1)的符合均匀分布的随机数数组
np.random.random((3, 2))

# 产生正态分布的随机数数组
np.random.randn(2)
np.random.randn(2, 4)

# randint(low,high,size),返回范围在[low,high)之间的size个整数
np.random.randint(1, 10, 8)  # array([1, 5, 1, 1, 1, 5, 6, 7])


# ====================  分布随机数生成  =======================
# 产生二项分布的随机数
np.random.binomial(10, 0.5, (2, 3))  # 第1个参数表示均值,2表示方差,3表示矩阵的size
# 产生卡方分布的随机数
np.random.chisquare(2, (2, 3)) 		 # 第1个参数表示自由度
# gama伽马分布
np.random.gamma(2, 4, 100)  		 # 前两个参数表示自由度
# 正态分布
np.random.normal(0, 0.1, 5)  		 # 第1个参数表示均值,2为标准差,3为返回值的维度
# 均匀分布
np.random.uniform(0, 5, 2)
# 泊松分布
np.random.poisson(5, 2)
```



#### 随机操作

```python
# ====================  随机抽样操作  =======================
# 从np.arange(5)数组中抽取3个数
np.random.choice(5, 4)  # array([0, 0, 2, 0])

# 不放回抽样,抽取数组中不会有重复值
np.random.choice(5, 4, replace=False)  # array([4, 3, 2, 1])

# 被抽取数组中的元素具有不同概率
np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])  # 概率对应每个元素array([0, 1, 2, 3, 4])  ==>  array([3, 2, 3])

# ====================  随机排列操作  =======================
# 洗牌操作
a = np.arange(5)
np.random.shuffle(a)  # array([0, 2, 1, 3, 4])

# 返回随机序列
np.random.permutation([1, 2, 3, 4])  # array([2, 1, 4, 3])
```





## Pands数据分析库

Pands是一个强大的分析结构化数据的工具集, 它是基于Numpy, 可用于数据挖掘和数据分析, 同时也提供数据清洗的功能.



### 数据结构

- **Series**
  - Series是一种类似于一维数组的对象, 是由一组数据(各种NumPy数据类型)以及一组与之相关的数据标签(即索引)组成.
- **DataFrame**
  - DataFrame是一个表格型的数据结构, 它含有一组有序的列, 每列可以是不同的值类型.
  - DataFrame既有行索引, 也有列索引, 可看做是Series组成的字典, 每个Series看做DataFrame的一个列.
- Pandas中这两种结构里很多属性和方法是一样的.



#### 创建series

```python
# 1.直接创建
pd.Series([1, 2, 3, np.nan, 9, 0])

# 2.数组创建,默认带索引
pd.Series(np.array(['a', 'b', 'c']))

# 3.字典创建,若不指定索引,则索引为字典的键
pd.Series({'a': 1, 'b': 2, 'c': 3})


# 通过Series的values和index属性获取其数组表示形式和索引对象
s = pd.Series(np.array(['a', 'b', 'c']))
s.values  # array(['a', 'b', 'c'], dtype=object)
s.index   # RangeIndex(start=0, stop=3, step=1)
```



#### 创建DataFrame

```python
# 1.通过字典创建DataFrame
pd.DataFrame({'A': 1.,
              'B': pd.Timestamp('2021-01-01'),  # Timestamp 方法生成时间戳
              'C': pd.Series(1, list(range(4)), dtype='float32'),
              'D': np.array([3] * 4),
              #  Categoricals 是 pandas 的一种数据类型, 对应着被统计的变量,具有特定的顺序, 这个顺序是创建时手工设定的, 是静态的
              'E': pd.Categorical(["test", "train", "test", "train"]),
              'F': 'foo'})


# 2.通过时间序列创建DataFrame
# 生成作为行索引的时间序列,start为日期起点,end为日期终点,periods为个数,freq表示间隔(D表示以日为间隔)  
dates = pd.date_range(start="2021-01-01", end="2021-02-01", periods=7)
pd.DataFrame(np.random.randn(7, 5), index=dates, columns=list("ABCDE"))
'''
                        A	        B	        C	        D	        E
2021-01-01 00:00:00	0.750120	-0.094547	-0.459937	0.767405	-1.748746
2021-01-06 04:00:00	-2.362144	-0.702300	0.476891	0.031054	-0.021801
2021-01-11 08:00:00	0.764357	0.662128	0.340510	-0.194788	-0.826951
2021-01-16 12:00:00	0.378670	0.437846	0.671887	1.355264	-0.896017
2021-01-21 16:00:00	-0.357642	-0.053722	0.958072	-0.288953	1.743930
2021-01-26 20:00:00	-0.279510	0.251506	0.496458	-2.000370	0.576176
2021-02-01 00:00:00	1.659798	1.079884	0.255388	-0.142203	1.559521
'''
```





### 常用操作

```python
import numpy as np
import pands as pd

# 示例
data = np.arange(15).reshape([3, 5])
df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D', 'E'])
print(df)
'''
    A   B   C   D   E
a   0   1   2   3   4
b   5   6   7   8   9
c  10  11  12  13  14
'''

# 显示前n条数据
print(df.head(2))
'''
   A  B  C  D  E
a  0  1  2  3  4
b  5  6  7  8  9
'''

# 显示底部的n条数据
print(df.tail(1))
'''
    A   B   C   D   E
c  10  11  12  13  14
'''

# 获取索引
print(df.index)  # Index(['a', 'b', 'c'], dtype='object')

# 修改索引
df.index = [1, 2, 3]

# 获取列
print(df.columns)  # Index(['A', 'B', 'C', 'D', 'E'], dtype='object')

# 修改列名
df.columns = ['A2', 'B2', 'C2', 'D2', 'E2']

# 获取所有数据
df.values  # array([[ 0,  1,  2,  3,  4],[ 5,  6,  7,  8,  9],[10, 11, 12, 13, 14]])

# 只能通过行号索引,获取一行的数据
df.iloc[1]
'''
A    5
B    6
C    7
'''

# 根据列名对相关索引进行切片操作,获取一列的数据
df.loc['a':'c':2, 'A']  # 获取A列,索引为a到c(包括c)中的数据,步长为2
'''
a     0
c    10
'''

# 查看数据的详细信息
(df.describe()
'''
           A     B     C     D     E
count   3.0   3.0   3.0   3.0   3.0       # 一列的元素个数               
mean    5.0   6.0   7.0   8.0   9.0       # 一列数据的平均值 
std     5.0   5.0   5.0   5.0   5.0       # 一列数据的均方差,反映一个数据集的离散程度              
min     0.0   1.0   2.0   3.0   4.0       # 一列数据中的最小值            
25%     2.5   3.5   4.5   5.5   6.5       # 一列数中的最大值            
50%     5.0   6.0   7.0   8.0   9.0       # 一列数据中, 前 25% 的数据的平均值            
75%     7.5   8.5   9.5  10.5  11.5       # 一列数据中, 前 50% 的数据的平均值            
max    10.0  11.0  12.0  13.0  14.0       # 一列数据中, 前 75% 的数据的平均值            
'''
```



### 数据对齐

Pandas最重要的一个功能是, 它可以对不同索引的对象进行算术运算; 在将对象相加时, 如果存在不同的索引对, 则结果的索引就是该索引对的并集.

> **自动的数据对齐操作在不重叠的索引处引入NaN值.**

```python
s1 = pd.Series([1, 2, -9], index=['a', 'b', 'c'])
s2 = pd.Series([1, 34, 434, 3], index=['a', 'f', 'b', 'n'])
print(s1 + s2)
'''
a      2.0
b      436.0
c      NaN
f      NaN
n      NaN
'''
```



### 映射操作

> **DataFrame的apply方法, 可以将函数应用到由各列或行所形成的一维数组上.** 

```python
df = pd.DataFrame(np.arange(9).reshape([3, 3]), columns=['A', 'B', 'C'])

# 定义函数
func = lambda x: x.sum()

# 加载函数到df中
reslut = df.apply(func)
print(reslut)
```



### 数据操作

```python
# 使用drop方法删除不需要的列或行
a = df.drop(['a'], axis=0)
b = df.drop(['A'], axis=1)

# 使用append方法合并两个DataFrame
c = a.append(b)
print(c)
'''
      A   B   C   D   E
b   5.0   6   7   8   9
c  10.0  11  12  13  14
a   NaN   1   2   3   4
b   NaN   6   7   8   9
c   NaN  11  12  13  14
'''

# 使用iteritems方法遍历每列数据,返回一个包含列名称和列内容为Series的元组
n = 1
for s in df.iteritems():
    print("第%d列数据%s" % (n, s))
    n += 1
'''
第1列数据('A', a     0
b     5
c    10
Name: A, dtype: int32)
第2列数据('B', a     1
b     6
c    11
Name: B, dtype: int32)
'''

# 还原索引,让索引变为数据中的一列,可以对索引列进行操作  
df.reset_index()  
'''
   index  A  B  C
0      0  0  1  2
1      1  3  4  5
2      2  6  7  8
'''
```



### 统计函数 

```python
# ====================  分组聚合统计  =======================
'''
 先根据某列分组,然后再对某列进行聚合统计计算
'''
df = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
# 根据c列进行分组,计算a列的总分和平均分
df.groupby('c')['a'].agg([np.sum, np.mean])


# ====================  索引排序  =======================
'''
 根据任意一个轴上的索引进行排序,默认按升序,指定ascending=False为降序
'''
df = pd.DataFrame(np.arange(8).reshape([2, 4]), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
print(df)
'''
       d  a  b  c
three  0  1  2  3
one    4  5  6  7
'''
# 对索引列的名字进行排序
print(df.sort_index(ascending=False))
'''
       d  a  b  c           
one    4  5  6  7           
three  0  1  2  3           
'''
# 对字段列的名字进行排序
print(df.sort_index(axis=1, ascending=False))
'''
       a  b  c  d
three  1  2  3  0
one    5  6  7  4
'''


# ====================  名次排序 =======================
''' 
 根据每行数据的大小返回名次
 DataFrame.rank（axis = 0, method ='average', numeric_only = None, na_option ='keep', ascending = True, pct = False ） 
 axis选择行或列,
 method ='average'表示对平均值排名（可以取一下几个值'average', 'min', 'max', 'first', 'dense'）, 
 ascending = True表示降序排序, 
 na_option ='keep'表示将NA值保留在原来的位置
'''
s3 = pd.Series(np.random.randn(5), index=list('abcde'))
s3.rank()


# ====================  计算当前元素和先前元素之间的百分比变化  =======================
'''
 函数将每个元素与其前一个元素进行比较,并计算百分比变化
 DataFrame.pct_change（periods= 1, fill_method ='pad', limit = None, freq = None, ** kwargs ）：
 periods为形成百分比变化的时期, 
 fill_method为如何在计算百分比变化之前处理NA, 
 limit表示停止前要填充的连续NA的数量 
'''
s = pd.Series([1, 2, 3, 4, 5, 4, 2])
print(s.pct_change())


# ====================  计算协方差  =======================
'''
 计算列的协方差,不包括NA/null值
 Series.cov（min_periods = None）
 min_periods表示每个列对所需的最小观测值数
'''
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print(s1.cov(s2))

# 当应用于DataFrame时, 则需要计算所有列之间的协方差(cov)值. 
df = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print(df.cov())
```



### 缺失值操作

```python
# 示例
df2 = pd.DataFrame(np.random.rand(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])


# 1.使用reindex方法设置新的索引,多出的索引对应数据使用NaN填充
df3 = df2.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
'''
        one       two     three
a  0.505405  0.476354  0.232798
b       NaN       NaN       NaN
c  0.945555  0.684889  0.989451
d       NaN       NaN       NaN
e  0.168444  0.284992  0.137487
f  0.904736  0.756874  0.819553
'''


# 2.检查每列的数据是否存在缺失,返回True/False
df3['one'].isnull()
''''
a    False
b     True
c    False
d     True
'''


# 3.缺失数据的计算,求和数据时,NaN将被视为0; 如果数据全部是NaN,那么结果将是NaN
df3['one'].sum()


# 4.使用指定数据来替换NaN值
'''
 DataFrame.fillna（value = None,method = None,axis = None,inplace = False,limit = None,downcast = None,** kwargs ）
 使用指定的方法和数据填充NA/NaN值,
 Value表示填充数据,
 method表示填充方法（'backfill','bfill','pad','ffill',None）
'''
df3.fillna(0)
'''
        one       two     three
a  0.896954  0.004486  0.398638
b  0.000000  0.000000  0.000000
c  0.011506  0.058437  0.850751
d  0.000000  0.000000  0.000000
e  0.473934  0.642129  0.368234
f  0.895597  0.313774  0.140006
g  0.000000  0.000000  0.000000
h  0.126904  0.620270  0.813192
'''


# 5.删除带有NaN的数据
'''
DataFrame.dropna（axis = 0,how ='any',thresh = None,subset = None,inplace = False ）
 How表示删除的方式（any：删除存在NA值的行或列；all：删除整行/列全部都为NA的列或行）
'''
df3.dropna()
```





### 文件读写

| 函数           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| read_csv       | 从文件、URL、文件型对象中加载带分隔符的数据.默认分隔符为逗号 |
| read_table     | 从文件、URL、文件型对象中加载带分隔符的数据.默认分隔符为制表符 |
| read_fwf       | 读取定宽列格式数据（即无分隔符）                             |
| read_clipboard | 读取剪贴板中的数据, 可以看作read_table的剪贴板版.再将网页转换为表格时很有用 |
| read_excel     | 从XLS或xlsx文件读取表格数据, 读写excel文件时需要安装依赖xlrd |
| read_html      | 读取HTML文档中的所有表格                                     |
| read_json      | 读取JSON字符串中的数据                                       |

```python
# ====================  读写csv文件  =======================
# 读取csv文件
r = pd.read_csv("test.csv",
                sep="\t", 			   		 # 指定分隔符
                names=['A', 'B', 'C', 'D'],  # 修改头表对应的列名,空列用NaN代替
                index_col='D',  			 # 指定索引列
                header='infer',  			 # 将文件第一行默认为列名
                encoding='utf-8', 	    	 # 指定编码格式
                )

# 写入csv文件
r.to_csv(
    "re_test.csv",
    sep='\t',    			  # 指定分隔符
    mode='w',  				  # 写入模式
    columns=['A', 'B', 'C'],  # 指定写入的列,若读取时D列指定为索引列,则写入时D列不存在
    index_label='label', 	  # 指定索引名称
)



# ====================  读写excel文件  =======================
# 读取excel文件
e = pd.read_excel("test.xlsx",
                  sheet_name='Sheet3',    # 指定工作表
                  names=['A', 'B', 'C'],  # 修改头表对应的列名,空列用NaN代替
                  header=0, 			  # 指定列名
                  index_col=None,  		  # 指定索引列
                  )

# 写入excel文件
e.to_excel(
    "re_test.xlsx",
    sheet_name='Sheet3',  				  # 指定工作表
    columns=['A', 'B', 'C'],  			  # 指定写入的列
    index_label='序号',  			   	     # 指定索引名称
)
```







## Matplotlib数据可视化库

### 1.导包

```python
# Matplotlib绘图包
import matplotlib.pyplot as plt

# 3D绘图包
from mpl_toolkits.mplot3d import  Axes3D

# 解决中文不显示问题
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
```





### 2.创建画布

在绘图结构中, Figure创建画布, Subplot创建子图.

- Figure: 面板(画布), matplotlib中所有图像都位于figure对象中, 一个图像只能有一个figure对象.
- Subplot: 子图, figure对象下创建一个或多个subplot对象(即axes)用于绘制图像.
  - matplotlib.pyplot.subplot(*args, **kwargs) , `*args`是三个独立整数(画布行数, 画布列数, 选中号), 用于描述子图的位置.

```python
# 1.创建一个8x6大小的图像,dpi=80表示分辨率每英尺80点
plt.figure(figsize=(8, 6), dpi=80)

# 2.设置画布背景,有5种主题选择
'''
暗网格(seaborn-darkgrid)
白网格(seaborn-whitegrid)
全黑(seaborn-dark)
全白(seaborn-white)
全刻度(seaborn-ticks)
'''
plt.style.use("seaborn-whitegrid")

# 3.数据源
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 4.将画布分为2行1列两个子图,选中第1个子图做数据配置
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')

# 5.选中第2个子图做数据配置
plt.subplot(212)
plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()
```





### 3.选择图表

| 图形       | 对应函数      |
| ---------- | ------------- |
| 折线图     | plt.plot()    |
| 条形图     | plt.bar()     |
| 横向条形图 | plt.barh()    |
| 直方图     | plt.hist()    |
| 散点图     | plt.scatter() |
| 饼图       | plt.pie()     |
| 箱线图     | plt.boxplot() |

```python
# ====================  折线图  =======================
plt.figure(dpi=100)
x=np.linspace(0,20,10)
plt.plot(x, color="blue", linewidth=1, label="Blue", linestyle="--")
plt.show()


# ====================  散点图  =======================
a = np.random.randint(0, 20, 15)
b = np.random.randint(0, 20, 15)
plt.figure(dpi=100)
plt.scatter(a, b) 
plt.show()


# ====================  条形图  =======================
level = ['优秀', '不错', '666']
x = range(len(level))
y = [1, 3, 2]
plt.figure(dpi=100)
plt.bar(x, y, width=0.5, color=['b', 'r', 'g'])
plt.xticks(x, level)
plt.grid(linestyle="--", alpha=0.5)
plt.show()


# ====================  直方图  =======================
t = np.random.randint(0, 30, 90)
plt.figure(dpi=100)
distance = 2  # 设置组距
group_num = int((max(t) - min(t)) / distance)  # 计算组数
plt.hist(t, facecolor="blue", edgecolor="black", alpha=0.7)
plt.xticks(range(min(t), max(t))[::2])
plt.show()
```





### 4.设置图表细节

**图表函数中的参数大致都通用.**



#### 坐标轴样式

> plt.xlim()显示的是x轴的作图范围, 而plt.xticks()表达的是x轴的刻度内容的范围.

```python
# ====================  范围设置  =======================
# 设置x轴范围
plt.xlim(-4.0, 4.0)  
# 设置y轴范围
plt.ylim(-1.0, 1.0)  


# ====================  刻度设置  =======================
# 设置x轴刻度以及对应的刻度标签
plt.xticks(np.linspace(-4, 4, 3, endpoint=True),['优秀', '不错', '666'])  
# 设置y轴刻度
plt.yticks(np.linspace(-1, 1, 3, endpoint=True))  


# ====================  轴标签名设置  =======================
# 设置x轴的标签名
plt.xlabel('x')
# 设置y轴的标签名
plt.ylabel('y')
# 设置图表的标签名
plt.title('t')
```



#### 图例

> 配合图表函数中定义的`label`参数使用.

| 图例标签位置 | 数值 |
| ------------ | ---- |
| best  (默认) | 0    |
| upper right  | 1    |
| upper left   | 2    |
| lower left   | 3    |
| lower right  | 4    |
| right        | 5    |
| center left  | 6    |
| center right | 7    |
| lower center | 8    |
| upper center | 9    |
| center       | 10   |

```python
# 调用legend方法使图表函数中定义的label生效,label设置图例标签名称
plt.plot(x, s, color="green", linewidth=1.0, label="Green", linestyle="-.")

# ncol设置图例显示列数,loc设置位置,fontsize设置字体大小,title设置图例标题
plt.legend(ncol = 1, loc = 2, fontsize = 20, title = '图例标题)
```



#### 网格样式

```python
# axis='both'/'x'/'y'表示只显示横线和竖线/竖线/横线
plt.grid(axis='both',linestyle="--", alpha=0.5)
```



#### 颜色样式

| 颜色   | 别名 | HTML颜色名 |
| ------ | ---- | ---------- |
| 蓝色   | b    | blue       |
| 红色   | r    | red        |
| 绿色   | g    | green      |
| 黄色   | y    | yellow     |
| 青色   | c    | cyan       |
| 黑色   | k    | black      |
| 白色   | w    | white      |
| 洋红色 | m    | magenta    |

```python
# 设置颜色
color = 'r'

# 设置透明度
alpha = 0.5
```



#### 线条样式

| 线条风格      | 描述       |
| ------------- | ---------- |
| '-'           | 实线       |
| ':'           | 虚线       |
| '--'          | 破折线     |
| '-.'          | 点划线     |
| 'steps'       | 阶梯线     |
| 'None' / ', ' | 什么都不画 |

```python
# 设置线型
linestyle = '--'
ls = '--'

# 设置线宽
linewidth = 5
lw = 5
```



#### 数据点样式

| 标记 | 描述    |
| ---- | ------- |
| '.'  | 点      |
| '*'  | 星号    |
| '+'  | 加号    |
| ','  | 像素    |
| 'x'  | X       |
| 'o'  | 圆圈    |
| 'D'  | 菱形    |
| 'd'  | 小菱形  |
| 's'  | 正方形  |
| 'p'  | 五边形  |
| 'h'  | 六边形1 |
| 'H'  | 六边形2 |
| '8'  | 八边形  |

```python
# 设置数据点样式
marker = 's'

# 设置数据点大小
markersize = 10 
```





### 5.保存与展示

```python
# 保存图形
plt.savefig("数据图形.png",dpi = 100)

# 展示图形
plt.show()
```







### Seaborn

Seaborn是一种基于matplotlib的图形可视化工具, 在此基础上进行了更高级的API封装.



> 保留项目











## Requests请求库

Requests是python的一个HTTP请求库, 基于python中的urllib模块实现.



### 请求对象

| 请求方式                 |
| ------------------------ |
| requests.get(url)        |
| requests.post(url, data) |
| requests.put(url)        |
| requests.delete(url)     |
| requests.head(url)       |
| requests.options(url)    |

> get请求与post请求的区别
>
> - http的method字段不同.
> - post可以附加body, 可以支持form、json、 xml、binary等各种数据格式.
> - **无状态变化的建议使用get请求**, 如请求多次结果一致, 不涉及信息修改.
> - **数据的写入与状态修改建议用post请求**.

```python
# ====================  参数设置  =======================
# 请求参数
data = {'from': 'zh',
        'to': 'en',
        'query': '人生苦短'}
# 请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', }
# 代理ip
proxies = {"http": "http://100.10.1.10:3128", "https": "http://100.10.1.10:1080"}
# cookies
cookies = {"cookies" = "2348298091kjshfksu18239j..."}
# 请求URL
url = 'https://fanyi.baidu.com'
# 传递URL参数: URL + ? + 键值对
url = 'https://fanyi.baidu.com?%s=%s' % (tuple(data.keys())[2], data["query"])

# ====================  get请求  =======================
response1 = requests.get(url,  					# 请求url
                        params=data,  			# 请求参数
                        headers=headers,  		# 请求头
                        proxies=proxies,  		# 代理ip
                        timeout=5,  			# 超时参数
                        verify=True, 			# 避免ssl证书问题
                        cookies=cookies,        # cookies
                        allow_redirects=False,  # 禁用重定向
                        )


# ====================  post请求  =======================
response2 = requests.post(url,
                         data=data,
                         headers=headers,
                         proxies=proxies,
                         headers=headers,  		 
                         proxies=proxies,  		 
                         timeout=5,  			 
                         verify=True, 			 
                         cookies=cookies,         
                         allow_redirects=False,   
                         )
```



#### SSL证书验证

Requests可以为HTTPS请求验证SSL证书, 就像web浏览器一样, SSL验证默认是开启的, 如果证书验证失败, Requests会抛出SSLError.为了避免这种情况的发生可以通过`verify=False`, 但是这样是可以访问到页面, 但是会提示：**InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.** 

```python
import requests

# 解决方案
from requests.packages import urllib3
urllib3.disable_warnings()    			# 就这一句就可以解决

response = requests.get("https://www.12306.cn",verify=False)
print(response.status_code)
```





### 响应对象

| API                         | 描述                                                      |
| --------------------------- | --------------------------------------------------------- |
| response.text               | 返回Unicode类型的响应主体,主要取文本                      |
| response.content            | 返回二进制的响应主体,主要取图片和文件等,中文显示为字符    |
| response.status_code        | 返回状态码                                                |
| response.reason             | 返回状态原因                                              |
| response.headers            | 返回响应头                                                |
| response.request.headers    | 返回请求消息的报头                                        |
| response.encoding           | 返回编码方式                                              |
| response.cookies            | 返回cookies                                               |
| response.url                | 返回请求URL                                               |
| response.history            | 访问重定向的历史记录,返回按照从老到近的请求进行排序的列表 |
| response.raise_for_status() | 响应码不为200时抛出异常                                   |
| response.raw                | 原始响应体, urllib的HTTPResponse对象                      |
| response.json()             | 转换成json格式数据                                        |
| response.elapsed            | 发送请求到接收到响应所花费的时长                          |
| response.close              | 关闭连接                                                  |





### 页面状态码

```python
100: ('continue',),
101: ('switching_protocols',),
102: ('processing',),
103: ('checkpoint',),
122: ('uri_too_long', 'request_uri_too_long'),
200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\o/', '✓'),
201: ('created',),
202: ('accepted',),
203: ('non_authoritative_info', 'non_authoritative_information'),
204: ('no_content',),
205: ('reset_content', 'reset'),
206: ('partial_content', 'partial'),
207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
208: ('already_reported',),
226: ('im_used',),

Redirection.
300: ('multiple_choices',),
301: ('moved_permanently', 'moved', '\o-'),
302: ('found',),
303: ('see_other', 'other'),
304: ('not_modified',),
305: ('use_proxy',),
306: ('switch_proxy',),
307: ('temporary_redirect', 'temporary_moved', 'temporary'),
308: ('permanent_redirect',
'resume_incomplete', 'resume',), # These 2 to be removed in 3.0

Client Error.
400: ('bad_request', 'bad'),
401: ('unauthorized',),
402: ('payment_required', 'payment'),
403: ('forbidden',),
404: ('not_found', '-o-'),
405: ('method_not_allowed', 'not_allowed'),
406: ('not_acceptable',),
407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
408: ('request_timeout', 'timeout'),
409: ('conflict',),
410: ('gone',),
411: ('length_required',),
412: ('precondition_failed', 'precondition'),
413: ('request_entity_too_large',),
414: ('request_uri_too_large',),
415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
417: ('expectation_failed',),
418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
421: ('misdirected_request',),
422: ('unprocessable_entity', 'unprocessable'),
423: ('locked',),
424: ('failed_dependency', 'dependency'),
425: ('unordered_collection', 'unordered'),
426: ('upgrade_required', 'upgrade'),
428: ('precondition_required', 'precondition'),
429: ('too_many_requests', 'too_many'),
431: ('header_fields_too_large', 'fields_too_large'),
444: ('no_response', 'none'),
449: ('retry_with', 'retry'),
450: ('blocked_by_windows_parental_controls', 'parental_controls'),
451: ('unavailable_for_legal_reasons', 'legal_reasons'),
499: ('client_closed_request',),

Server Error.
500: ('internal_server_error', 'server_error', '/o\', '✗'),
501: ('not_implemented',),
502: ('bad_gateway',),
503: ('service_unavailable', 'unavailable'),
504: ('gateway_timeout',),
505: ('http_version_not_supported', 'http_version'),
506: ('variant_also_negotiates',),
507: ('insufficient_storage',),
509: ('bandwidth_limit_exceeded', 'bandwidth'),
510: ('not_extended',),
511: ('network_authentication_required', 'network_auth', 'network_authentication'),
```



### 案例

爬取疫情数据, 并使用图表展示数据.

```python
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
```

