"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_map = {}
        return self.helper(head,node_map)
        
    def helper(self,head,node_map):
        if not head: return None
        if head in node_map: return node_map[head]
        new_head = Node(head.val, None,None)
        node_map[head] = new_head
        new_next = self.helper(head.next,node_map)
        new_random = self.helper(head.random,node_map)
        new_head.next = new_next
        new_head.random = new_random
        return new_head
