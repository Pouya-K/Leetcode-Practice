from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                if node.val not in visited:
                    visited.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        visited.sort()
        return visited[k-1]