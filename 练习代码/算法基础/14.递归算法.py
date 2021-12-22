# def F(n):
#     """求n的阶乘"""
#     if n == 1:
#         return n
#     return n*F(n-1)
# print(F(5))

# def climb_stairs(n):
#
#     """爬楼梯"""
#     if n ==1 or n==2:
#         return n
#     return climb_stairs(n-1) + climb_stairs(n-2)

# def climbStairs(n):
#     """递推式"""
#     if n <= 2:
#         return n
#
#     s = [1, 2]
#     for i in range(3, n + 1):
#         s[0], s[1] = s[1], s[0] + s[1]
#     return s[1]
#
# print(climbStairs(9))

'''1. 题目
有 5 个人坐在一起，问第五个人多少岁？
他说比第 4 个人大 2 岁。
问第 4 个人岁数，他说比第 3 个人大 2 岁。
问第 3 个人，又说比第 2 人大两岁。
问第 2 个人，说比第一个人大两岁。
最后问第 1 个人，他说是 10 岁。
请问第五个人多大？'''
# def howold(n):
#     if n == 1:
#         return 10
#     return howold(n-1) + 2
#
# print(howold(5))
