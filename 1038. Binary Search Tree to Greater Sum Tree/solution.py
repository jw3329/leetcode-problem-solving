# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # perform right
        # sofar + curr add 
        # perform left
        self.sofar = 0
        def dfs(curr):
            if not curr: return
            dfs(curr.right)
            curr_val = curr.val
            curr.val += self.sofar
            self.sofar += curr_val
            dfs(curr.left)
        
        dfs(root)
        return root
