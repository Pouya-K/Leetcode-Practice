def topKFrequent(nums, k):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] = hashmap[num] + 1
        else:
            hashmap[num] = 1
    sortedHash = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
    output = []
    for x in range(k):
        output.append(sortedHash[x][0])
    return output
