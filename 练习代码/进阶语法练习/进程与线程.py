from random import randint
from time import time, sleep
from multiprocessing import Process
from threading import Thread, Lock
from os import getpid
from multiprocessing import Queue

"""
未使用进程
"""


# def download_task(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     download_task('Python从入门到住院.pdf')
#     download_task('Peking Hot.avi')
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()


"""
使用了进程
"""


# def download_task2(filename):
#     print('启动下载进程，进程号：[%d]'%getpid())
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     p1 = Process(target=download_task2, args=('Python从入门到住院.pdf',))
#     p1.start()
#     p2 = Process(target=download_task2, args=('Peking Hot.avi',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()

"""
题目三:实现两个进程间的通信。我们启动两个进程，一个输出Ping，一个输出Pong，
两个进程输出的Ping和Pong加起来一共10个
"""


# def sub_task(string, counter):
#     while not counter.empty():
#         print(string, end=' ', flush=True)
#         counter.get()
#         sleep(0.01)
#
#
# def main():
#     counter = Queue()
#     for i in range(10):
#         counter.put(1)
#     Process(target=sub_task, args=('Ping',counter,)).start()
#     Process(target=sub_task, args=('Pong',counter,)).start()
#
#
# if __name__ == '__main__':
#     main()
# 预期结果：Ping Pong Pong Ping Ping Pong Pong Ping Pong Ping ，满足要求

'''
Python中的多线程
'''
# def download_task2(filename):
#     print('启动下载进程，进程号：[%d]'%getpid())
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     p1 = Thread(target=download_task2, args=('Python从入门到住院.pdf',))
#     p1.start()
#     p2 = Thread(target=download_task2, args=('Peking Hot.avi',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()


# 自定义线程类

# class Mythread(Thread):
#     def __init__(self, filename):
#         super().__init__()
#         self.filename = filename
#
#     def run(self):
#         print('启动下载进程，进程号：[%d]' % getpid())
#         print('开始下载%s...' % self.filename)
#         time_to_download = randint(5, 10)
#         sleep(time_to_download)
#         print('%s下载完成! 耗费了%d秒' % (self.filename, time_to_download))
#
# def main():
#     start = time()
#     p1 = Mythread('Python从入门到住院.pdf')
#     p1.start()
#     p2 = Mythread('Python从入门到住院.pdf')
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()

"""
线程锁的使用：解决线程之间的竞争问题
"""


class Account(object):

    def __init__(self):
        self._balance = 0
        self.lock = Lock()

    def deposit(self, money):
        # 计算存款后的余额
        try:
            self.lock.acquire()
            new_balance = self._balance + money
            # 模拟受理存款业务需要0.01秒的时间
            sleep(0.01)
            # 修改账户余额
            self._balance = new_balance
        finally:
            self.lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()