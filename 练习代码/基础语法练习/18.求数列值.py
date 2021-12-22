# 1. 题目
# 求 s=a+aa+aaa+aaaa+aa...a 的值，其中 a 是一个数字。例如 2+22+222+2222+22222（此时共有 5 个数相加），几个数相加由键盘控制。
#
# 2. 分析
# 关键是计算出每一项的值。
# Sn = 0
# for t in range(1,4)
import unittest
from selenium import webdriver

from functools import reduce
a = int(input('请输入数值：'))
n = int(input('请输入次数：'))
Sn = []
Tn = 0
for i in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

Sn = reduce(lambda x, y: x + y, Sn)
print("计算和为：", Sn)
