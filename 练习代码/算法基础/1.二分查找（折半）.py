def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items)-1
    while start <= end:
        mid = (start + end)//2
        if key < items[mid]:
            end = mid-1
        elif key > items[mid]:
            start = mid + 1
        else:
            return mid

    return -1



# def bin_search(items, key):
#     """折半查找"""
#     start, end = 0, len(items) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if key > items[mid]:
#             start = mid + 1
#         elif key < items[mid]:
#             end = mid - 1
#         else:
#             return mid
#     return -1


list = [1, 3, 5, 6, 10, 12, 15, 19]
print(bin_search(list, 5))
