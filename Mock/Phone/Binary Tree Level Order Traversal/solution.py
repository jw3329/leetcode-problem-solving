# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = [root]
        while queue:
            temp = []
            level = []
            while queue:
                curr = queue.pop(0)
                if curr.left: temp.append(curr.left)
                if curr.right: temp.append(curr.right)
                level.append(curr.val)
            res.append(level)
            queue = temp
        return res
