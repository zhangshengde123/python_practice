# def countingSort(arr, maxValue):
#     bucketLen = maxValue+1
#     bucket = [0]*bucketLen
#     sortedIndex =0
#     arrLen = len(arr)
#     for i in range(arrLen):
#         if not bucket[arr[i]]:
#             bucket[arr[i]]=0
#         bucket[arr[i]]+=1
#     for j in range(bucketLen):
#         while bucket[j]>0:
#             arr[sortedIndex] = j
#             sortedIndex+=1
#             bucket[j]-=1
#     return arr
def countingSort(arr, maxvalue):
    arrlen = len(arr)
    index = 0
    bucketlen = maxvalue + 1
    bucket = [0] * bucketlen
    for i in range(arrlen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketlen):
        while bucket[j] > 0:
            arr[index] = j
            index = index + 1
            bucket[j] -= 1
    return arr

arr = [2, 4, 3, 5, 8, 6, 3, 5, 7, 6]
countingSort(arr, 8)
print(arr)

def countingSort2(arr, maxValue):
    arrlen = len(arr)
    bucketlen = maxValue + 1
    bucket = [0]*bucketlen
    index = 0
    for i in range(arrlen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketlen):
        while bucket[j] > 0:
            arr[index] = j
            index += 1
            bucket[j] -= 1

arr = [2, 4, 3, 5, 8, 6, 3, 5, 7, 6]
countingSort2(arr, 8)
print(arr)


