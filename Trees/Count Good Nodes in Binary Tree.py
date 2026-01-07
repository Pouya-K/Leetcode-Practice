# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 1
        
        def dfs(root: TreeNode, maxValue):
            if not root:
                return
            
            nonlocal goodNodes
            if root.val >= maxValue:
                goodNodes += 1
            
            dfs(root.left, max(root.val, maxValue))
            dfs(root.right, max(root.val, maxValue))

        dfs(root.left, root.val)
        dfs(root.right, root.val)
        
        return goodNodes