def selectionSort(array, size):
    for val in range(size):
        minvalue = val
        for i in range(val+1, size):
            if(arr[i]<arr[minvalue]):
                minvalue = i
        (array[val],array[minvalue]) = (array[minvalue], array[val])

arr = [6,3,5,2,9,4]
length = len(arr)

print("Original Array is:",arr)
selectionSort(arr, length)
print("After swapping", arr)