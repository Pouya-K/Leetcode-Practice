class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'}': '{', ']' : '[', ')': '()'}

        for letter in s:
            if letter in brackets:
                if stack and stack[-1] == brackets[letter]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(letter)
        
        return True if stack is None else False
