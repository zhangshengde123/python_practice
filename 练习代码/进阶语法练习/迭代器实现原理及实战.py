"""
1.可迭代对象
能够被for ... in循环遍历的对象被称为可迭代对象iterable,列表、元组、集合均属于可迭代对象
2.尽可能使用for...in进行遍历，也可使用do...while进行遍历，
3.集合不支持通过访问索引来操作

"""

# #1.遍历列表代码
# list01 = [12, 'naisi', 'com', 'ddt']
# for i in list01:
#     print(i)
#
# print("-------------------分界线-------------------------")
# #1.遍历元组代码
# list02 = (12, 'naisi', 'com', 'ddt')
# for i in list02:
#     print(i)
#
# print("-------------------分界线-------------------------")
# #1.遍历元组代码
# list03 = {12, 'naisi', 'com', 'ddt'}
# for i in list03:
#     print(i)
# print("-------------------分界线-------------------------")
#
# #使用while进行遍历
# i = 0
# while i <len(list01):
#     string = list01[i]
#     print(string)
#     i = i + 1
#
# print("-------------------分界线-------------------------")
# """
# 2.迭代器iterator
#   迭代器iterator是一个特殊的对象，用来遍历可迭代对象iterable.
#
# """
# #列表的迭代器
# list_02 = [45, 354, "dhf", "我的"]
# listIterator = iter(list_02)
# while True:
#     try:
#         item = next(listIterator)
#         print(item)
#     except StopIteration:
#         break

"""
3.迭代协议
   使用迭代器遍历访问可迭代对象，要求迭代器和可迭代对象遵循迭代协议：
   
1.可迭代对象iterable提供成员方法__iter__，该方法用于遍历的迭代器iterator
2.迭代器 iterator 提供成员方法 __next__，该方法返回下一个被遍历的元素
3.异常 StopIteration，当遍历完全部的元素后，成员方法 __next__ 抛出一个特殊的异常 Stop Iteration 表示遍历结束
4.内置函数 iter，用于获取可迭代对象对应的迭代器
5.内置函数 iter，用于获取可迭代对象对应的迭代器
"""
# class Iterable:
#     #成员方法—__iter__
#     def __iter__(self):
# class Iterable:
#     #成员 __next__ 方法
#     def __next__(self):

#内置函数iter
# def iter(iterable):
#     iterator = iterable.__iter__()
#     return iterator
# #内置函数next
# def next(iterator):
#     item = iterator.__next__()
#     return item

#for...in 等价的代码如下
# iterator = iter(iterable)
# while True:
#     try:
#         item = next(iterator)
#         print(item)
#     except StopIteration:
#         breakpoint()

"""
4.实现一个自定义的迭代器
4.1  通过单链表实现堆栈
4.2实现迭代协议
4.3使用for...in循环遍历堆栈
"""
# 4.1通过一个链表实现堆栈


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def __iter__(self):
        return StackIterator(self)


stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")

# 4.2实现迭代协议


class StackIterator:

    def __init__(self, stack):
        self.stack = stack
        self.cursor = self.stack.head

    def __next__(self):
        if self.cursor == None:
            raise StopIteration
        else:
            item = self.cursor.item
            self.cursor = self.cursor.next
            return item


# 4.3通过for...in 循环遍历堆栈
for item in stack:
    print(item)




