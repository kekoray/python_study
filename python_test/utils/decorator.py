from functools import wraps
import re
import time


def Count(func, *args, **kwargs):
    @wraps(func)
    def wrapper(path, *args, **kwargs):
        with open("./log/log.txt", "a") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\t" + re.split(r"\\", path)[-1] + "\n")
            func(path, *args, **kwargs)
        return wrapper
