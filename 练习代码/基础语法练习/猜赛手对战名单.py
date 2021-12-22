

# 两个乒乓球队进行比赛，各出三人。
# 甲队为 a,b,c 三人，乙队为 x,y,z 三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a 说他不和 x 比，c 说他不和 x,z 比，请编程序找出三队赛手的名单。请编程序找出三队赛手的名单
import itertools
first = ('a', 'b', 'c')
second = ('x', 'y', 'z')
check_list = [('a', 'x'), ('c', 'x'), ('c', 'z')]

for i in itertools.permutations(first, 3):
    f = lambda a, b: len([True for j in zip(a, b) if j not in check_list])
    if f(i, second) == 3:
        print(list(zip(i, second)))