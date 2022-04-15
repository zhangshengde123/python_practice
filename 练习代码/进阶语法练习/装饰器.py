from functools import wraps
import functools
import time
import random

# def logit(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # 打开logfile，并写入内容
#             with open(logfile, 'a') as opened_file:
#                 # 现在将日志打到指定的logfile
#                 opened_file.write(log_string + '\n')
#             return func(*args, **kwargs)
#
#         return wrapped_function
#
#     return logging_decorator
#
#
# @logit()
# def myfunc1():
#     pass
#
#
# myfunc1()
#
#
# # Output: myfunc1 was called
# # 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串
#
# @logit(logfile='func2.log')
# def myfunc2():
#     pass
#
#
# myfunc2()
# # Output: myfunc2 was called
# # 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串


"""
1.使用装饰器实现日志打印器
"""
# def logger(func):
#     def warpper(*args, **kwargs):
#         # print('我准备开始计算：{} 函数了:'.format(func.__name__))
#         print(f'开始执行{func.__name__}')
#         func(*args, **kwargs)
#         print("执行结束")
#     return warpper
#
# @logger
# def multiply(x, y):
#     print(f'{x} * {y} = {x*y}')
#
#
# multiply(2, 4)

"""
2.使用装饰器实现时间计数器
"""


# def timer(func):
#     def warpper(*args, **kwargs):
#         t1 = time.time()
#         func(*args, **kwargs)
#         t2 = time.time()
#         t = int(t2-t1)
#         print(f'你一共花费了{t}秒')
#     return warpper
#
#
# @timer
# def want_sleep(second):
#     time.sleep(second)
#
#
# want_sleep(10)


"""

3.进阶用法：带参数的函数装饰器

"""


# def say_hello(country):
#
#     def warpper(func):
#
#         def demo(*args, **kwargs):
#             if country == '中国':
#                 print("你好！")
#             elif country == '美国':
#                 print("hi! hello")
#             else:
#                 pass
#             func(*args, **kwargs)
#         return demo
#     return warpper
#
#
# @say_hello('中国')
# def china():
#     print("I am come from China")
#
#
# @say_hello('美国')
# def america():
#     print("I am come from america")
#
#
# china()
# print("--------------------")
# america()

"""

4.高阶用法：不带参数的类装饰器

"""


# class Logger(object):
#     def __init__(self, func):
#         self.func =func
#
#     def __call__(self, *args, **kwargs):
#         print(f'[INFO]:function {self.func.__name__} is running!')
#         return self.func(*args, **kwargs)
#
#
# @Logger
# def say(request):
#     print(f'say {request}')
#
#
# say("hello")

"""

5.高阶用法：带参数的类装饰器

"""

# class Logger2(object):
#     def __init__(self, level="INFO"):
#         self.level = level
#
#     def __call__(self, func):
#         def warpper(*args, **kwargs):
#             print(f'[{self.level}]:the function {func.__name__} is running')
#             func(*args, **kwargs)
#         return warpper
#
#
# @Logger2(level="WARN")
# def demo(request):
#     print(f'say {request}')
#
#
# demo("严重警告")

"""
06. 使用偏函数与类实现装饰器
"""


# class DelayFunc():
#     def __init__(self,duration, func):
#         self.duration = duration
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print(f'等待{self.duration}秒后执行')
#         time.sleep(self.duration)
#         return self.func(*args, **kwargs)
#
#     def prompt(self, *args, **kwargs):
#         print(f"立即执行")
#         return self.func(*args, **kwargs)
#
#
# def delay(duration):
#
#     #装饰器，延迟某个函数的执行，同时也提供了prompt立即执行
#
#     return functools.partial(DelayFunc, duration)
#
# class DelayFunc2():
#
#     def __init__(self, duration, func):
#         self.duration = duration
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print(f'等待{self.duration} seconds 后.....')
#         time.sleep(self.duration)
#         return self.func(*args, **kwargs)
#
#     def eager_call(self, *args, **kwargs):
#         return self.func(*args, **kwargs)
#
#
# def delay2(duration):
#     return functools.partial(DelayFunc2, duration)
#
#
# @delay2(duration=4)
# def add(a, b):
#     print(a + b)
#
#
# add(3, 6)

"""
7.能装饰类的装饰器：实现类的单例模式

"""


# def Singleton(cls):
#
#     _instance = {}
#
#     def _singleton(*args, **kwargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kwargs)
#         return _instance[cls]
#     return _singleton
#
#
# @Singleton
# class A(object):
#     a = 1
#
#     def __init__(self, x=0):
#         self.x = x
#
#
#
# a1 = A(2)
# a2 = A(3)
# print(a1)
# print(a2)

"""
 8.functools .wraps 装饰器:
     它的作用就是将 被修饰的函数(wrapped) 的一些属性值赋值给 修饰器函数(wrapper) ，最终让属性的显示更符合我们的直觉。
"""


# def warpper(func):
#     @wraps(func)
#     def inner_func():
#         pass
#     return inner_func
#
#
# @warpper
# def warpped():
#     pass


# print(warpped.__name__)
#  不加wraps,打印出来的函数名是inner_func
#  加wraps后,打印出来的函数名是：warpped  更符合我们的直觉


"""
9.内置装饰器：
  它通常存在于类中，可以将一个函数定义成一个属性，属性的值就是该函数return的内容。
"""


# class Student(object):
#
#     def __init__(self, name):
#         self.name = name
#         # self.age = age
#         # self.grade = grade
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         self._age = value
#
#
# xiaoming = Student("小明")
#
# xiaoming.age = 25
# print(xiaoming.age)

"""
    有一个通过网络获取数据的函数（可能会因为网络原因出现异常），
    写一个装饰器让这个函数在出现指定异常时可以重试指定的次数，
    并在每次重试之前随机延迟一段时间，最长延迟时间可以通过参数进行控制。
"""

# 方法一：使用带参数的函数装饰器


def retry(*, times=3, wait_time=3, error=(Exception, )):

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except error:
                    time.sleep(wait_time*random.random())
            return None
        return wrapper
    return decorate

# 方法2：使用带参数的类装饰器


class Retry(object):

    def __init__(self, times, wait_time, error=(Exception, )):
        self.times = times
        self.wait_time = wait_time
        self.error = error

    def __call__(self,func):

        def wrapper(*args, **kwargs):
            for i in range(self.times):
                try:
                    return func(*args, **kwargs)
                except self.error:
                    time.sleep(self.wait_time*random.random())
            return None

        return wrapper






