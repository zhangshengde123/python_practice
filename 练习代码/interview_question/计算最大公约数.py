import math
# 计算最大公约数
# def max_yueshu(x, y):
#     max,min = x,y
#     if min > max:
#         max, min = min, max
#     if max % min == 0:
#         return min
#     else:
#         return max_yueshu(min, max%min)


# print(max_yueshu(75, 255))




#寻找列表最大的两个数

def find_max_two(list2):
    max_two = []
    list2.sort()
    long = len(list2)-1
    for i in range(2):
        max_two.append(list2.pop(long))
        long =long -1
    return max_two



def find_max_two_2(list2):
    max_two = []
    list3 = list2.copy()
    for i in range(2):
        max_two.append(max_value(list3))
        list3.remove(max_value(list3))
    return max_two

def max_value(arr):
    value = arr[0]
    for i in arr:
        if value < i:
            value, i = i, value
    return value


def find_max_two_3(item):
    a, b = item[0], item[1]
    if a < b:
        a, b = b, a
    for i in range(2, len(item)-1):
        if item[i] > a:
            b = a
            a = item[i]
        elif item[i] > b:
            b = item[i]
    return a, b









# def find_max_two_2(list2):
#     max_two = []
#     for i in range(2):
#         max_two.append(max(list2))
#         list2.remove(max(list2))
#     return max_two




list1 = list([0, 1, 354, 59, 22, 145, 0, 1, 3, 5])


# print(max_value(list1))

# print(find_max_two_2(list1))
# print(list1)


print(find_max_two_3(list1))
# print(find_max_two(list1))
# list1.sort()
# print(list1.pop(len(list1)-1))

# print(list1.pop())

# print(max(2,4,7,8,56))