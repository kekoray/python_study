


# 条件判断
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
for x in range(11):   # range(11)表示生成1到10的整数集合
    sum+=x
    print(sum)  # 每次循环都执行
print(sum)  # 打印sum最终结果


# while循环
sum = 0
a = 10
while a > 0 :
    print('OK --> ' + str(a))
    sum+=a
    a-=2
print(sum)


# break











