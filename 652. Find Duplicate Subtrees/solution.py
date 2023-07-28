# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # traverse and serialize
        res = []
        count_map = dict()
        
        def helper(root):
            if not root: return '#'
            s = f'{root.val},{helper(root.left)},{helper(root.right)}'
            count = count_map.get(s, 0) + 1
            count_map[s] = count
            if count == 2:
                res.append(root)
            return s
        
        helper(root)
        return res
