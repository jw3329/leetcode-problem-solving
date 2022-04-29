# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # dfs curr root, store into set, if k - val in set, then return true
        return self.dfs(root, k, set())
    
    def dfs(self, root, k, num_set):
        if not root: return False
        if k - root.val in num_set: return True
        num_set.add(root.val)
        return self.dfs(root.left, k, num_set) or self.dfs(root.right, k, num_set)
