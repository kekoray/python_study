import schedule
import time


def job():
    print("=====> job")


schedule.every(2).seconds.do(job)

# 每隔十分钟执行一次
# schedule.every(10).minutes.do(job)

# # 每隔一小时执行一次
# schedule.every().hour.do(job)

# # 每周一执行一次
# schedule.every().monday.do(job)

# # 每分钟的第44秒执行一次
# schedule.every().minute.at(":44").do(job)

# # 每天的18:50执行一次
# schedule.every().day.at("18:50").do(job)

# # 每周天的18:50执行一次
# schedule.every().sunday.at("18:50").do(job)

print("==========")

if __name__ == '__main__':
    n = 0
    while True:
        # 调度启动
        schedule.run_pending()
        time.sleep(1)
        n += 1
        if n > 10:
            break

    

    print("==========")
