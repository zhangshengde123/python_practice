def seq_search(items, key):

    """
    使用了enumerate函数
    enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    """
    for index, item in enumerate(items):
        if item == key:
            return index

    return -1


# def seq_search(items, key):
#     index = 0
#     for item in items:
#         if item == key:
#             return index
#         else:
#             index +=1
#     return -1

mylist = [1, 3, 5, 9, 12, 14, 16, 19]
print(seq_search(mylist, 19))

