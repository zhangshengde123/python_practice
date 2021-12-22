

"""推导式使用：
生成式（推导式）可以用来生成列表、集合和字典
"""
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
#
# prices2 = {key:value for key,value in prices.items() if value > 200}
# print(prices2)

# names = ["李白", "杜埔", "王维", "李贺", "陶渊明"]
# poems = ["《静夜思》", "《采菊》", "《行路难》", "《无题》", "饮酒"]
#
# scores = [[None] * len(poems) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(poems):
#         scores[row][col] = float(input(f'请输入{name}的{poems}成绩: '))
#         print(scores)




"""
   heapq模块（堆排序）
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(2, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, lambda x: x['shares']))
print(heapq.nsmallest(2, list2, lambda x: x['price']))


"""
迭代工具模块 itertools模块
"""