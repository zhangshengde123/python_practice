# def insert_sort(arr):
#     """插入排序，从小到大排序"""
#     if len(arr) <= 1:
#         return arr
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j = j-1
#         arr[j+1] = key
# def insert_sort(arr):
#     """从大到小排序"""
#     if len(arr)<= 1:
#         return arr
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j>=0 and key > arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#
#
# arr1 = [12, 11, 13, 5, 6]
# insert_sort(arr1)
# for i in range(len(arr1)):
#     print("%d" % arr1[i])


# def insertionSort(arr):
#     for i in range(1, len(arr)):
#
#         key = arr[i]
#
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
#
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i])


def insertSort(arr):
    if len(arr) < 1:
        return arr
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = key





arr = [12, 11, 13, 5, 6]
insertSort(arr)
for i in range(len(arr)):
    print(arr[i])





