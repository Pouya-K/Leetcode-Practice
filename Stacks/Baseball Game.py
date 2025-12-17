from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        output = 0

        for operation in operations:
            if operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int (operation))
        
        for num in stack:
            output += num

        return output
     