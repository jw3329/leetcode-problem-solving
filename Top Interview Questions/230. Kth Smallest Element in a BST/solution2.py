# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(root):
            if root.left: helper(root.left)
            self.count -= 1
            if not self.count:
                self.number = root.val
                return
            if root.right: helper(root.right)
        self.count = k
        self.number = 0
        helper(root)
        return self.number
