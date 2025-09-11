def twoSum(nums, target):
    hashmap = {}
    for x in range(len(nums)):
        num = nums[x]
        if (target - num) in hashmap:
            return [hashmap[target - num], x]
        hashmap[num] = x
    return
