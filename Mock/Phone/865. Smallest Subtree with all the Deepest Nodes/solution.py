# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.node_map = {}
        self.node_map[None] = -1
        # record all node_map, node: depth
        self.record_all_map(root,None)
        self.max_depth = -1
        for depth in self.node_map.values():
            self.max_depth = max(self.max_depth, depth)
        
        return self.get_deepest(root)
    
    def record_all_map(self,root,parent):
        if not root: return
        self.node_map[root] = self.node_map[parent] + 1
        self.record_all_map(root.left,root)
        self.record_all_map(root.right,root)
        
    def get_deepest(self,root):
        if not root: return None
        if self.node_map[root] == self.max_depth: return root
        
        left_deepest = self.get_deepest(root.left)
        right_deepest = self.get_deepest(root.right)
        
        if left_deepest and right_deepest: return root
        if left_deepest: return left_deepest
        if right_deepest: return right_deepest
        return None
