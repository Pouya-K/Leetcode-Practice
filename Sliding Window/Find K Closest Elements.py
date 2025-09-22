def findClosestElements(arr, k, x):
    l = 0
    r = len(arr) - 1
    while r - l >= k:
        if abs(x - arr[l]) <= abs(x - arr[r]):
            r -= 1
        else:
            l += 1
    return arr[l:r+1]


print(findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))
