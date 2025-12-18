class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        numOfDots = 0
        s = ""

        for i in range(len(path)):
            s = path[i]
            
            if s == ".":
                numOfDots += 1

            if stack[-1] != "/" or s != "/":
                stack.append(s)

            if (1 <= numOfDots <= 2 and s == "/") or i == len(path) - 1:
                if numOfDots == 1:
                    if s == "/":
                        stack.pop()
                    if stack[-2] == "/":
                        stack.pop()
                if numOfDots == 2:
                    if s == "/":
                        stack.pop()
                    if (stack[-3] == "/"):
                        stack.pop()
                        stack.pop()
                        if len(stack) != 1: 
                            stack.pop()
                        
                        while stack and stack[-1] != "/":
                            stack.pop()

            if s != ".":
                numOfDots = 0

        if len(stack) != 1 and stack[-1] == "/":
            stack.pop()
        return "".join(stack)
    
solution = Solution()
print(solution.simplifyPath("/..//_home/a/b/..///"))