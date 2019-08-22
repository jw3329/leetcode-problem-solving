# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.flatten(root.left)
        self.flatten(root.right)
        if not root.left: return
        flattened_left = root.left
        root.left = None
        curr = flattened_left
        while curr.right: curr = curr.right
        curr.right = root.right
        root.right = flattened_left
