def select_sort(arr):

    for i in range(len(arr)):
        minindex = i
        for j in range(i+1, len(arr)):
            if arr[minindex] > arr[j]:
                minindex = j
        if arr[minindex] != arr[i]:
            arr[minindex], arr[i] = arr[i], arr[minindex]
    return arr


arr1 = [3, 12, 11, 13, 5, 6]

select_sort(arr1)
for i in range(len(arr1)):
    print(arr1[i])

