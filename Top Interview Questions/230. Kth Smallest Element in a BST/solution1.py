# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = []
        self.helper(root,count)
        return count[k-1]
    
    def helper(self,root,count):
        if not root: return
        self.helper(root.left,count)
        count.append(root.val)
        self.helper(root.right,count)
