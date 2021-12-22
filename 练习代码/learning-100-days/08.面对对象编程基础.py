"""
 #定义一个类
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study(self):
        print(f'{self.name}正在学习英语')
    def watch_movie(self):
        if self.age > 18:
            print(f"{self.name}可以看七龙珠")
        if self.age <= 18:
            print(f"{self.name}可以看海贼王")

stu1 = Student("小明", 13)
stu1.study()
stu1.watch_movie()

"""
"""
# 访问可见性问题
class Test():
    def __init__(self, foo):
        self.__foo = foo
    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello,world')
    test._Test__bar()
    print(test._Test.__foo)


if __name__ == '__main__':
    main()
"""
"""面对对象三大支柱；封装、继承、多态"""
# from time import time,sleep
#
#
# class Clock(object):
#     """定义一个数字时钟类"""
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def nowtime(self):
#         time()
#
#     def run(self):
#         """展示时间"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def showtime(self):
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
# def main():
#     clock = Clock(23,58,58)
#     while True:
#         print(clock.showtime())
#         sleep(1)
#         clock.run()
#
# if __name__ == '__main__':
#     main()


#练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。

import math
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self,x,y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def instance(self,other):
        dx = self.x-other.x
        dy = self.y - other.y
        distance2 = dx**2 + dy**2
        distance = math.sqrt(distance2)
        print('两点间的距离为%d' % distance)

    def show(self):
        return '(%d,%d)' %(self.x, self.y)

def main():
    point1 = Point(2,4)
    point2 = Point()
    point1.move_by(3, 1)
    print(point1.show())
    point1.move_to(6,8)
    print(point1.show())
    point1.instance(point2)

if __name__ == "__main__":
    main()









