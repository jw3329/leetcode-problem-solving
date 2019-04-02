# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        index_node_dict = {}
        i=1
        cur = head
        while cur:
            index_node_dict[i] = cur
            cur = cur.next
            i += 1
        if i-n-1 not in index_node_dict:
            return head.next
        next_node = None
        if i-n+1 in index_node_dict:
            next_node = index_node_dict[i-n+1]
        index_node_dict[i-n-1].next = next_node
        return head
