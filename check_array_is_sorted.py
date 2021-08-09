def isArraySorted(arr):
    if len(arr) == 1:
        return True

    return arr[0] < arr[1] and isArraySorted(arr[1:])


arr = [1, 2, 3, 4, 5, 3, 7, 8, 9, 10]
print(isArraySorted(arr))
