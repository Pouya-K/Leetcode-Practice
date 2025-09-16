def checkInclusion(s1:str, s2:str):
    s1Letters, s2Letters = [0] * 26, [0] * 26
    if len(s1) > len(s2):
        return False
    for x in range(len(s1)):
        s1Letters[ord(s1[x]) - ord('a')] += 1
        s2Letters[ord(s2[x]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        if s1Letters[i] == s2Letters[i]:
            matches += 1
    leftPointer = 0
    rightPointer = len(s1) - 1
    while rightPointer < len(s2) - 1:
        print(matches)
        if matches == 26:
            return True

        index = ord(s2[leftPointer]) - ord('a')
        s2Letters[index] -= 1
        if s1Letters[index] == s2Letters[index]:
            matches += 1
        elif s1Letters[index] == s2Letters[index] + 1:
            matches -= 1

        leftPointer += 1
        rightPointer += 1

        index = ord(s2[rightPointer]) - ord('a')
        s2Letters[index] += 1
        if s1Letters[index] == s2Letters[index]:
            matches += 1
        elif s1Letters[index] == s2Letters[index] - 1:
            matches -= 1
    print(matches)
    if matches == 26:
        return True
    return False

print(checkInclusion("abc", "bbbca"))