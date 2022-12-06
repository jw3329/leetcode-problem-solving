# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = dict()
        seen[0] = dummy
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next
        prefix = 0
        head = dummy
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next
