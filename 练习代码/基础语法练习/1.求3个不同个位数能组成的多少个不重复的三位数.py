#
# 题目一：
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
sum = 0
t= 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i !=j and i !=k and j !=k:
                print(i, j, k)
                sum =sum +1

print(f"共能组成{sum}个不重复的三位数")


