# python学习



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
| `<=`  `<`  `>`  `>=`  `= =`  `!=`              | 比较运算符 |
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
# 重命名文件, rename(命名前，命名后)
os.rename("../kn/abc.py", "../kn/1.py")


''' ==================== os.path子模块 ==================== '''
# 返回绝对路径
os.path.abspath("path")
# 文件存在则返回 True,不存在返回 False
os.path.exists("path")
# 返回文件大小，如果文件不存在就返回错误
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
# 洗牌，打乱序列
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





## 正则表达式





### 特殊符号

| 表示法 | 描述 | 匹配的表达式 | 结果 |
| ------ | ---- | ------------ | ---- |
|        |      |              |      |
|        |      |              |      |
|        |      |              |      |
|        |      |              |      |
|        |      |              |      |
|        |      |              |      |



### 字符

| 表示法 | 描述 |
| ------ | ---- |
|        |      |
|        |      |
|        |      |
|        |      |







#### 常见的正则表达式

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |



#### 注意事项

- 原始字符串













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









## Numpy





```

```



