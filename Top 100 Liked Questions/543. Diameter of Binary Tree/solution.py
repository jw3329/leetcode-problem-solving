# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0
        self.max_depth(root)
        return self.max
    
    def max_depth(self,root):
        if not root: return 0
        left_max = self.max_depth(root.left)
        right_max = self.max_depth(root.right)
        self.max = max(self.max, left_max + right_max)
        return max(left_max,right_max) + 1
