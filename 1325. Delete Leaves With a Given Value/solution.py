# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def helper(root):
            if not root: return None
            left = helper(root.left)
            right = helper(root.right)
            if left or right:
                root.left = left
                root.right = right
                return root
            if root.val == target: return None
            root.left = None
            root.right = None
            return root
        
        return helper(root)
