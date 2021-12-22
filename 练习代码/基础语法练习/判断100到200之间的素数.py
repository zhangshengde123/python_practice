# 判断 101-200 之间有多少个素数，并输出所有素数。
#
# 2. 分析
# 判断素数的方法：用一个数分别去除 2 到 sqrt（这个数），如果能被整除，则表明此数不是素数，反之是素数。
from math import sqrt
total = 0
leap = 1
for i in range(100, 201):
    t = int(sqrt(i + 1))
    for j in range(2, t + 1):
        if i % j == 0:
            leap = 0
            break
    if leap == 1:
        print(i)
        total = total + 1
    leap = 1
print(f'共有{total}个素数')



