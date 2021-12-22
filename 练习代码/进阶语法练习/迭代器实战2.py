import os


"""
要求完成如下任务：

统计文件有多少个单词
统计文件中每个单词出现的频率
"""
# 使用直接遍历法；1.统计单词个数
# file = open('test.txt')
# count = 0
# while True:
#     line = file.readline()
#     if not line:
#         break
#     words = line.split()
#     for item in words:
#         print(item)
#         count += 1
#
# print(f"共有{count}个单词")


# 2.统计文件中每个单词出现的次数

# file = open('test.txt')
# dict = {}
#
# while True:
#     line = file.readline()
#     if not line:
#         break
#     words = line.split()
#     for item in words:
#         if item in dict:
#             dict[item] += 1
#         else:
#             dict[item] = 1
# for item, count in dict.items():
#     print('%s : %d' % (item, count))
"""
二、使用迭代器方法
3.1 可迭代对象与迭代器
本题目实现类iterateWord用于将文本中的单词，他计算可迭代对象，也是迭代器。
作为可迭代对象，提供了__iter__方法，防护了一个迭代器
作为迭代器，提供了__next__方法，返回下一个遍历的对象

"""


class Iterateword:
    def __init__(self, file):
        self.file = file
        self.words = []

    #实现iter方法
    def __iter__(self):
        return self

    #实现next方法

    def __next__(self):
        if len(self.words) == 0:
            self.get_non_blank_line()
        word = self.words.pop(0)
        return word

    #get_non_blank_line方法读取一个非空的行
    def get_non_blank_line(self):
        while True:
            line = file.readline()
            if not line:
                raise StopIteration
            self.words = line.split()
            if len(self.words) != 0:
                break

"""
3.1使用迭代器统计单词个数
"""
file = open('test.txt')
count = 0
for word in Iterateword(file):
    print(word)
    count = count + 1


"""
3.2使用迭代器统计单词个数
"""
# dict = {}
# for word in Iterateword(file):
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1
#
# for word, count in dict.items():
#     print('%s :%d' %(word, count))