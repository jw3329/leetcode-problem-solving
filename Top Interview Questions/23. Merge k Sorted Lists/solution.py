# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = curr = ListNode(None)
        q = PriorityQueue()
        for idx, node in enumerate(lists):
            if node: q.put((node.val,idx,node))
        while not q.empty():
            _,idx,curr.next = q.get()
            curr=curr.next
            if curr.next: q.put((curr.next.val, idx, curr.next))
        return dummy.next
