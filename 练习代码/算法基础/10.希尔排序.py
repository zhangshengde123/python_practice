def shellSort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j= i
            while j >= gap and temp < arr[j-gap]:
                arr[j] = arr[j-gap]
                j = j-gap
            arr[j] = temp
        gap = gap//2



arr = [12, 34, 54, 2, 3, 6, 8, 11, 14]
# arr = [12, 34, 54, 2, 3]
n = len(arr)
# print("排序前:")
# for i in range(n):
#     print(arr[i]),

shellSort(arr)

print("\n排序后:")
for i in range(n):
    print(arr[i])



