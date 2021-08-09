# -*- coding: utf-8 -*- 
# @Time : 2021/8/9 17:31
# @Author : koray
# @File :


class p(object):

    # 可迭代对象,能被for循环遍历的对象
    # 可迭代对象不是迭代器,但是迭代器是可迭代对象
    # 迭代器协议: 实现对象的__iter__和__next__方法
    def __iter__(self):
        pass

    def __getitem__(self):
        pass

    # 返回容器的下一个元素
    def __next__(self):
        pass


if __name__ == '__main__':
    iter([1, 2])

# 生成器generator,是一类特殊的迭代器,性能上比迭代器好,
# 可以使用next和send取值,第一次取值时,需要用next
# 1.yield创建生成器


# 2.生成器表达式创建生成器
g = (x * 2 for x in range(5))
