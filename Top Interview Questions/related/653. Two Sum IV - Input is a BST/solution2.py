# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        
        def dfs(root):
            if not root: return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        
        dfs(root)
        left = 0
        right = len(arr) - 1
        while left < right:
            val = arr[left] + arr[right]
            if val == k: return True
            if val > k: right -= 1
            else: left += 1
        return False
