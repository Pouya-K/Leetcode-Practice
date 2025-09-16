def findRepeatedDnaSequences(s: str):
    repeatedDNA, foundDNA = set(), set()
    pointer = 0
    while pointer < (len(s) - 9):
        currentDNA = s[pointer:pointer+10]
        if currentDNA in foundDNA:
            repeatedDNA.add(currentDNA)
        else:
            foundDNA.add(currentDNA)
        pointer += 1
    return list(repeatedDNA)


print(findRepeatedDnaSequences("AAAAAAAAAAAAAAAAAAAAAAAA"))
