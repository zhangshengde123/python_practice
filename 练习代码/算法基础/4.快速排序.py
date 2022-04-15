# def partition(arr, low, high):
#     i = (low - 1)  # 最小元素索引
#     pivot = arr[high]
#
#     for j in range(low, high):
#
#         # 当前元素小于或等于 pivot
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引
# # 快速排序函数
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
# def quickSort(arr, left, right):
#     if left < right:
#         pi = partition(arr, left, right)
#         quickSort(arr, left, pi-1)
#         quickSort(arr, pi+1, right)
#     return arr
#
#
# def partition(arr, left, right):
#     pivot = left
#     index = pivot + 1
#     i = index
#     while i <= right:
#         if arr[i] < arr[pivot]:
#             arr[i], arr[index] = arr[index], arr[i]
#             index += 1
#         i += 1
#     arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
#
#     return index-1
def partition(arr, left, right):
    pivot = left
    index = pivot
    i = index
    for j in range(i+1, right + 1):
        if arr[j] < arr[pivot]:
            arr[j], arr[index] = arr[index], arr[j]
            index += 1
    arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
    return index-1


def quickSort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quickSort(arr, left, pi-1)
        quickSort(arr, pi+1, right)
    return arr



arr = [3, 5, 14, 9, 6, 7]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr[i])