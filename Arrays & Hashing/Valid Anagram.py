class Solution:
    def isAnagram(self, t, s) -> bool:
        if len(t) != len(s):
            return False
        countedLettersS = {}
        countedLettersT = {}
        for i in range(len(s)):
            countedLettersS[s[i]] = 1 + countedLettersS.get(s[i], 0)
            countedLettersT[t[i]] = 1 + countedLettersT.get(t[i], 0)
        return countedLettersT == countedLettersS
