class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range (len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                num = ""

                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * substring)
        
        return "".join(stack)