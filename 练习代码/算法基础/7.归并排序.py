# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#
#     # 创建临时数组
#     L = [0] * (n1)
#     R = [0] * (n2)
#
#     # 拷贝数据到临时数组 arrays L[] 和 R[]
#     for i in range(0, n1):
#         L[i] = arr[l + i]
#
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
#
#     # 归并临时数组到 arr[l..r]
#     i = 0  # 初始化第一个子数组的索引
#     j = 0  # 初始化第二个子数组的索引
#     k = l  # 初始归并子数组的索引
#
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#
#     # 拷贝 L[] 的保留元素
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#
#     # 拷贝 R[] 的保留元素
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
#
#
# def mergeSort(arr, l, r):
#     if l < r:
#         m = int((l + (r - 1)) / 2)
#
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
#         merge(arr, l, m, r)

# def merge_sort(arr):
#       """归并排序"""
#       if len(arr) == 1:
#           return arr
#       # 使用二分法将数列分两个
#       mid = len(arr) // 2
#       left = arr[:mid]
#       right = arr[mid:]
#       # 使用递归运算
#       return merge(merge_sort(left), merge_sort(right))
#
#
# def merge(left, right):
#      """排序合并两个数列"""
#      result = []
#      # 两个数列都有值
#      while len(left) > 0 and len(right) > 0:
#          # 左右两个数列第一个最小放前面
#          if left[0] <= right[0]:
#              result.append(left.pop(0))
#          else:
#              result.append(right.pop(0))
#      # 只有一个数列中还有值，直接添加
#      result += left
#      result += right
#      return result

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


# arr1 = [1,4,6,9]
# arr2 = [2,5,8,45,]
# arr3 = merge(arr1, arr2)
# print(arr3)











# arr = [11, 99, 33 , 69, 12, 88, 55, 11, 33, 36,39, 66, 44, 22]
arr = [11, 99, 33 , 69, 12, 88]
print(merge_sort(arr))
