def lengthOfLongestSubstring(s):
    maxLen = 0
    leftPointer = 0
    usedLetters = set()
    for rightPointer in range(len(s)):
        while s[rightPointer] in usedLetters:
            usedLetters.remove(s[leftPointer])
            leftPointer += 1
        usedLetters.add(s[rightPointer])
        maxLen = max(maxLen, rightPointer - leftPointer + 1)
    return maxLen
