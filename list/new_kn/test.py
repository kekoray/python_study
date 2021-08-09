# 异常处理
try:
    num = 0
    result = 1 / num
except Exception:
    print("num不能为0")
finally:
    print("程序结束..")


# 自定义异常,通过继承Exception类实现,使用raise调用自定义异常

class MyException(Exception):

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


def func(age):
    if 100 > age > 18:
        return 1
    else:
        raise MyException("未成年不准进入网吧")


if __name__ == '__main__':
    # func(16)  # __main__.MyException: 未成年不准进入网吧

    # assert断点调试
    # 在运行带有assert语句的脚本时,通过-O参数来屏蔽assert
    def foo(num):
        assert type(num) == int, "num 必须为整形"
        assert num != 0, 'n is zero!'
        return 10 / num


    foo(0)
