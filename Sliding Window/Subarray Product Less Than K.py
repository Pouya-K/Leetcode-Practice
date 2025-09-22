def numSubarrayProductLessThanK(nums, k):
    leftPointer = 0
    product = 1
    output = 0
    for rightPointer in range (len(nums)):
        product *= nums[rightPointer]
        while leftPointer <= rightPointer and product >= k:
            product //= nums[leftPointer]
            leftPointer +=1
        output += rightPointer - leftPointer + 1

    return output


print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))