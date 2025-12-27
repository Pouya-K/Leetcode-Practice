from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        queue = deque([root])

        while queue:
            currentLevel = []
            for i in range(len(queue)):
                node = queue.popleft()

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

                    currentLevel.append(node.val)


            if currentLevel:
                output.append(currentLevel)
        
        return output