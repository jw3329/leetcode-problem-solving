# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []
        
        def helper(root,is_root):
            if not root: return None
            deleted_root = root.val in to_delete_set
            if is_root and not deleted_root:
                res.append(root)
            
            root.left = helper(root.left,deleted_root)
            root.right = helper(root.right,deleted_root)
            
            return None if deleted_root else root
        
        helper(root,True)
        return res
