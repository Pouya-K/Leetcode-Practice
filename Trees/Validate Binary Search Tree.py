from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRec(root, float("-inf"), float("inf"))

    def isValidBSTRec(self, root: Optional[TreeNode], min, max):
        if not root:
            return True

        if not min < root.val < max:
            return False

        return self.isValidBSTRec(root.left, min, root.val) and self.isValidBSTRec(root.right, root.val, max)