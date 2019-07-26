# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        sorted_num = []
        self.dfs(root,sorted_num)
        start, end = 0, len(sorted_num) - 1
        while start < end:
            if sorted_num[start] + sorted_num[end] == k: return True
            elif sorted_num[start] + sorted_num[end] < k:
                start += 1
            else:
                end -= 1
        return False
    
    def dfs(self,root,sorted_num):
        if not root: return
        
        self.dfs(root.left,sorted_num)
        sorted_num.append(root.val)
        self.dfs(root.right,sorted_num)
