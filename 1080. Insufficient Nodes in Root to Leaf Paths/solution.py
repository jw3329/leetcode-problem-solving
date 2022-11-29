# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        # track from par to leaf
        # if leaf and less than limit, then mark as null
        # if no leaf anymore, then return to be deleted
        
        def helper(root, curr):
            if not root: return None
            if not root.left and not root.right:
                if curr + root.val < limit: return None
                return root
            left_purged = helper(root.left, curr + root.val)
            right_purged = helper(root.right, curr + root.val)
            # if none -> no path to leaf -> return none
            # if both purged is none -> return none
            if not left_purged and not right_purged: return None
            root.left = left_purged
            root.right = right_purged
            return root
        
        return helper(root, 0)
