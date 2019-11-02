# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_queue = [p]
        q_queue = [q]
        while p_queue and q_queue:
            p_curr = p_queue.pop(0)
            q_curr = q_queue.pop(0)
            if not p_curr and not q_curr: continue
            if not p_curr or not q_curr: return False
            if p_curr.val != q_curr.val: return False
            p_queue.append(p_curr.left)
            p_queue.append(p_curr.right)
            q_queue.append(q_curr.left)
            q_queue.append(q_curr.right)
        return True if not p_queue and not q_queue else False
