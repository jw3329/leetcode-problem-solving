# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root: return []
            return helper(root.left) + [root.val] + helper(root.right)
        
        # put into array first
        arr = helper(root)
        # sorted, so just compare diff of two
        min_val = sys.maxsize
        for i in range(1, len(arr)):
            min_val = min(min_val, arr[i] - arr[i-1])
        return min_val
