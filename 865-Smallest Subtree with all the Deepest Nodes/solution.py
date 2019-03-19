# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.depth = {}
        self.depth[None] = -1
        self.dfs(root, None)
        self.max_depth = -1
        for d in self.depth.values():
            self.max_depth = max(self.max_depth,d)
        return self.answer(root)
    
    def dfs(self,node,parent):
        if not node: return
        self.depth[node] = self.depth[parent] + 1
        self.dfs(node.left,node)
        self.dfs(node.right,node)
    
    def answer(self,node):
        if not node or self.depth[node] == self.max_depth: return node
        left_answer = self.answer(node.left)
        right_answer = self.answer(node.right)
        if left_answer and right_answer: return node
        if left_answer: return left_answer
        if right_answer: return right_answer
        return None
