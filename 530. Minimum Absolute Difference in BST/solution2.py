# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.prev = None
        self.min_val = sys.maxsize
        
        def helper(root):
            if not root: return self.min_val
            helper(root.left)
            if self.prev is not None:
                self.min_val = min(self.min_val, root.val - self.prev)
            self.prev = root.val
            helper(root.right)
            return self.min_val
        
        return helper(root)
