from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        output = defaultdict(list)
        for word in strs:
            frequencyArr = [0]*26
            for letter in word.lower():
                frequencyArr[ord(letter) - ord('a')] += 1
            
            output[tuple(frequencyArr)].append(word)
        
        return list(output.values())
