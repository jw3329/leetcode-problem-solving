"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [root]
        while queue:
            temp_queue = []
            while queue:
                cur = queue.pop(0)
                if not cur: continue
                temp_queue.append(cur.left)
                temp_queue.append(cur.right)
            for i in range(len(temp_queue)-1):
                if temp_queue[i]: temp_queue[i].next = temp_queue[i+1]
            queue = temp_queue
        return root
