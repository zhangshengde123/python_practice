def buildMaxHeap(arr):
    """从数组中间位置向左查找"""
    import math
    for i in range(math.floor(len(arr)/2), -1, -1):
        print(i)  #，输出结果 3 2 1 0
# math.floor(len(arr)/2),
# arr1 = [3, 12, 11, 13, 5, 6]
# a = buildMaxHeap(arr1)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left


def swap(arr, i, j):
    """交换位置"""
    arr[i], arr[j] = arr[j], arr[i]