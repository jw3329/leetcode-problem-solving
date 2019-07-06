# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_val = -sys.maxsize
        self.helper(root)
        return self.max_val
    
    def helper(self,root):
        if not root: return 0
        left = max(0,self.helper(root.left))
        right = max(0,self.helper(root.right))
        
        self.max_val = max(self.max_val, left + right + root.val)
        return max(left, right) + root.val
