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
        return self.copy_helper(head,node_map)
    
    def copy_helper(self,head,node_map):
        if not head: return None
        if head in node_map: return node_map[head]
        new_head = Node(head.val,None,None)
        node_map[head] = new_head
        new_head.next = self.copy_helper(head.next,node_map)
        new_head.random = self.copy_helper(head.random, node_map)
        return new_head
