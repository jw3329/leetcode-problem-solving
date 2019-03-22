# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        node_list = self.getNodeList(root)
        left, right = 0, len(node_list) - 1
        while left < right:
            if node_list[left].val + node_list[right].val == k: return True
            if node_list[left].val + node_list[right].val > k: right -= 1
            else: left += 1
        return False
    
    def getNodeList(self,root):
        if not root: return []
        return self.getNodeList(root.left) + [root] + self.getNodeList(root.right) 
