


# if判断
# 从上往下判断,如遇到true就执行当前代码,忽略后面代码.

a = 2
if a > 3:
    print('OK')
elif a == 2:
    print('yes')
else:
    print('no')

# 缩写, 只要x是非零数值,非空字符串,非空list等, 就判断为True.
x = 2
if x :
    print('This is no none.')



# for循环

sum = 0
for x in range(11):   # range(11)表示生成1到10的整数
    sum+=x
    print(sum)  # 每次循环都执行
print(sum)  # 打印sum最终结果

# range用法
range(101)     #  产生0到100范围的整数,需要注意的是取不到101.
range(1, 101)   #  产生1到100范围的整数,相当于前面是闭区间后面是开区间.
range(1, 101, 2)  #  产生1到100的奇数,其中2是步长,即每次数值递增的值.
range(100, 0, -2)  #  产生100到1的偶数,其中-2是步长,即每次数字递减的值



# while循环
sum = 0
a = 10
while a > 0 :
    print('OK --> ' + str(a))
    sum+=a
    a-=2
print(sum)


# break
# 提前退出循环.
n = 1
while n <= 100:
    if n > 10: # 当n = 11时,条件满足,执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')


# continue
# 跳过当前的这次循环.
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数,执行continue语句
        continue # continue语句会直接继续下一轮循环,后续的print()语句不会执行
    print(n)


# 函数
# 函数可以同时返回多个值,但其实就是一个tuple
# 函数参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# *args是可变参数,args接收的是一个tuple
# **kw是关键字参数,kw接收的是一个dict

# 定义函数的语法
def 函数名(参数):
    #方法体
    return

# 空函数
def nop():
    pass  # 什么都不做


# 定义函数
def add(*args):  
    total = 0 
    for val in args:
        total+=val
    return total

# 调用函数
print(add(1))
print(add(1,2))



# 由于Python没有函数重载,所以每个文件就代表了一个模块(module),在不同的模块中可有同名函数,通过import导入指定的模块就可以使用同名函数

# module1.py
def foo():
    print('hello, world!')

# module2.py
def foo():
    print('goodbye, world!')

# test.py
    # from module1 import foo
    # foo() # 输出hello, world!

    # from module2 import foo
    # foo() # 输出goodbye, world!





