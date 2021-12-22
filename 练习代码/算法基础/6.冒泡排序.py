def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr1 = [3, 12, 11, 13, 5, 6]

bubblesort(arr1)
for i in range(len(arr1)):
    print(arr1[i])




