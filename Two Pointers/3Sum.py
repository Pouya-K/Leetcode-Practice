def threeSum(nums):
    nums.sort()
    output = []
    for x in range(len(nums)):
        num1 = nums[x]
        if num1 > 0:
            break
        if x > 0 and num1 == nums[x-1]:
            continue
        leftPointer = x+1
        rightPointer = len(nums) - 1
        target = -num1
        while leftPointer < rightPointer:
            num2 = nums[leftPointer]
            num3 = nums[rightPointer]
            if (num2 + num3) < target:
                leftPointer += 1
            elif (num2 + num3) > target:
                rightPointer -= 1
            else:
                foundList = [num1, num2, num3]
                output.append(foundList)
                leftPointer += 1
                rightPointer -= 1
                while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                    leftPointer += 1

    return output


print(threeSum([-1, 0, 1, 2, -1, -4]))
