# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # bfs
        queue = deque([root])
        while queue:
            # same level confirming
            x_exist = False
            y_exist = False
            for _ in range(len(queue)):
                curr = queue.popleft()
                # make sure the condition is same
                if curr.val == x: x_exist = True
                if curr.val == y: y_exist = True
                # make sure to prevent same parent condition
                if curr.left and curr.right:
                    if curr.left.val == x and curr.right.val == y: return False
                    if curr.left.val == y and curr.right.val == x: return False
                # since same parent condition is passed, queue next level
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            # check if exist
            if x_exist and y_exist: return True
        return False
