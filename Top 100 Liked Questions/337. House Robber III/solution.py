# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.rob_helper(root))
    
    def rob_helper(self,root):
        if not root: return [0] * 2
        left = self.rob_helper(root.left)
        right = self.rob_helper(root.right)
        res = [0] * 2
        
        res[0] = max(left) + max(right)
        res[1] = root.val + left[0] + right[0]
        return res
