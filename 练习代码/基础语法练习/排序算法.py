'''1.冒泡排序'''

def bubblesort(arr):

    #计算数组长度
    n = len(arr)

    #遍历数组的所有元素，从数组的第一个数开始往后一一比较。大的交换到后面
    for i in range(0,n):
        for j in range(0,n-i-1):

