# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        vals = []
        queue = deque([root])
        while queue:
            val = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                val += curr.val
            vals.append(val)
        i = 0
        max_val = vals[0]
        for j in range(1, len(vals)):
            if max_val < vals[j]:
                max_val = vals[j]
                i = j
        return i + 1
