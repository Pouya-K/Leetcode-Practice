def numOfSubarrays(arr, k, threshold):
    subArraysFound = 0
    currentSum = 0
    for x in range(k - 1):
        currentSum += arr[x]

    for leftPointer in range(len(arr) - k + 1):
        currentSum += arr[leftPointer + k - 1]
        average = currentSum / k
        if average >= threshold:
            subArraysFound += 1
        currentSum -= arr[leftPointer]
    return subArraysFound


print(numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
