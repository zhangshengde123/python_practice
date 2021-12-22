
# 1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# list = [4, 3, 7, 2]
# account = 0
# for i in list:
#     for j in list:
#         for k in list:
#             if (i != j) and (j != k) and (i != k):
#                 print(i, j, k)
#                 account += 1
#
# print(f"共有{account}个符合要求")

# 2. 题目
# 企业发放的奖金根据利润提成。
#利润 (I) 低于或等于 10 万元时，奖金可提 10%；
# 利润高于 10 万元，低于 20 万元时，低于 10 万元的部分按 10% 提成，高于 10 万元的部分，可提成 7.5%；
# 20 万到 40 万之间时，高于 20 万元的部分，可提成 5%；40 万到 60 万之间时高于 40 万元的部分，可提成 3%；
# 60 万到 100 万之间时，高于 60 万元的部分，可提成 1.5%，高于 100 万元时，超过 100 万元的部分按 1% 提成；
# 从键盘输入当月利润 I，求应发放奖金总数？
# i = int(input("当前利润为："))
# bonus = 0
# if i <= 100000:
#     bonus = i/10
# elif (i >100000) and (i <= 200000):
#     bonus = 100000/10 +(i-100000)*0.075
# elif (i >200000) and (i <= 400000):
#     bonus = 100000*0.1 + 100000*0.075 +(i-200000)*0.05
# elif (i >400000) and (i <= 600000):
#     bonus = 100000*0.1 + 100000*0.075 + 200000*0.05 + (i-400000)*0.03
# elif (i >600000) and (i <= 1000000):
#     bonus = 100000*0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + (i-600000)*0.015
# elif i > 1000000:
#     bonus = 100000*0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + 400000*0.015 + (i-1000000)*0.01
# else:
#     pass
# print(f"应发的奖金总数为{bonus}")
# 3.输入某年某月某日，判断这一天是这一年的第几天？输入某年某月某日，判断这一天是这一年的第几天？

# year = int(input("请输入年份："))
# month = int(input("请输入月份："))
# day = int(input("请输入日期："))
# day_num = 0
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 1 < month <= 12:
#     day_num = months[month-1]
# else:
#     print("输入数据有误")
# day_num += day
# leap = 0
# if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
#     leap = 1
# if (leap == 1) and (month < 3):
#     day_num += 1
# print(f"今天是今年的第{day_num}天")
# 4.输入三个整数 x,y,z，请把这三个数由小到大输出。
# l =[]
# for i in range(3):
#     x = int(input("请输入整数："))
#     l.append(x)
# l.sort()
# # l.reverse()  逆向排序
# print(l)

# 5.斐波那契数列
"""输出第n个斐波那契数列"""
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#
#     return fib(n-1) + fib(n-2)
#print(fib(6))

"""输出前n个斐波那契数列"""
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
         fibs.append(fibs[-1] + fibs[-2])
    return fibs
print(fib(7))