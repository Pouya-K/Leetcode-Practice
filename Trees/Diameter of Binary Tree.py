from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        
        def dfsHeight(root: Optional[TreeNode]) -> int:
            nonlocal diam
            
            if not root:
                return 0

            leftHeight = dfsHeight(root.left)
            rightHeight = dfsHeight(root.right)
            diam = max(diam, leftHeight + rightHeight)
            
            return 1 + max(leftHeight, rightHeight)
    
        print(dfsHeight(root))
        return diam