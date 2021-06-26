def isArraySorted(arr):
    if len(arr) == 0:
        return True
    return arr[0] <= arr[1] and isArraySorted(arr[1:])    

arr = [1,2,3,4,5,6,7,8,9,10]
print(isArraySorted(arr))

