# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # par, grand
        
        def helper(root, par, grand):
            if not root: return 0
            res = 0
            if grand % 2 == 0:
                res += root.val
            return res + helper(root.left, root.val, par) + helper(root.right, root.val, par)
        
        return helper(root, -1, -1)
