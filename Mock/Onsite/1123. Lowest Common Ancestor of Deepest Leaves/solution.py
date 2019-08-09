# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # return the level of the node
        # compare level of the left and right 
        # if both level are same, then return root
        # if both level are not same, return the leaves of it
        
        return self.helper(root)[1]
        
    def helper(self,root):
        # return level, then node
        if not root:
            return 0, None
        left_level, left_lca = self.helper(root.left)
        right_level, right_lca = self.helper(root.right)
        if left_level > right_level: return left_level + 1, left_lca
        if right_level > left_level: return right_level + 1, right_lca
        return left_level + 1, root
