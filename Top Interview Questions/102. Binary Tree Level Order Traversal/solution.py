# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []
        while queue:
            partial_list = []
            new_queue = []
            while queue:
                cur = queue.pop(0)
                if not cur: continue
                partial_list.append(cur.val)
                new_queue += [cur.left,cur.right]
            if partial_list: res.append(partial_list)
            queue = new_queue
        return res
                
