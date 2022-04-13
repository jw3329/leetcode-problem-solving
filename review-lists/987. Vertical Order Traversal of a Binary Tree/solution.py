# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # height -> nodes map
        # return by iterating
        
        height_map = collections.defaultdict(list)
        row_map = dict()
        
        def helper(root, row, col):
            if not root: return
            height_map[col].append(root.val)
            row_map[root.val] = row
            helper(root.left, row + 1, col - 1)
            helper(root.right, row + 1, col + 1)
        
        
        helper(root, 0, 0)
        res = []
        for key in sorted(height_map.keys()):
            # append to map, same height
            # for list of same height, sort and append
            sub_map = collections.defaultdict(list)
            for val in height_map[key]:
                sub_map[row_map[val]].append(val)
            # order it
            sub_res = []
            # sort by rows
            for key in sorted(sub_map.keys()):
                val = sub_map[key]
                sub_res += sorted(val)
            res.append(sub_res)
        return res
