def characterReplacement(s, k):
    leftPointer = 0
    maxLength = 1
    letterCounts = {}
    for rightPointer in range(len(s)):
        letterCounts[s[rightPointer]] = 1 + letterCounts.get(s[rightPointer], 0)
        mostFrequentChar = max(letterCounts.values())

        while (rightPointer - leftPointer + 1 - mostFrequentChar) > k:
            letterCounts[s[leftPointer]] -= 1
            leftPointer += 1
        maxLength = max(maxLength, rightPointer - leftPointer + 1)

    return maxLength


print(characterReplacement("ABAB", 2))
