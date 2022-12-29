# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two step with one step, track prev, then next next of it
        # when selected, that is to be deleted
        hare = tortoise = head
        prev = None
        while hare and hare.next:
            prev = tortoise
            tortoise = tortoise.next
            hare = hare.next.next
        # now tortoise is to be deleted
        if not prev: return None
        prev.next = tortoise.next
        return head
