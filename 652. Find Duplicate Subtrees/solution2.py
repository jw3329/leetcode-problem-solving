# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        s_id_map = dict()
        id_count_map = dict()
        self.curr_id = 1
        
        def helper(root):
            if not root: return 0
            left_id = helper(root.left)
            right_id = helper(root.right)
            s = f'{root.val},{left_id},{right_id}'
            s_id = s_id_map.get(s, self.curr_id)
            if s_id == self.curr_id: self.curr_id += 1
            s_id_map[s] = s_id
            count = id_count_map.get(s_id, 0) + 1
            id_count_map[s_id] = count
            if count == 2:
                res.append(root)
            return s_id
        
        
        helper(root)
        return res
