# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.is_symmetric_helper(root.left,root.right)
    
    def is_symmetric_helper(self,root1,root2):
        if root1 and root2:
            if root1.val != root2.val: return False
            else:
                return self.is_symmetric_helper(root1.left, root2.right) \
            and self.is_symmetric_helper(root1.right,root2.left)
        else:
            if not root1 and not root2: return True
            else: return False
