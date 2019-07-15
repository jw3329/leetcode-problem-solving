# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head
        head_next = head.next
        sub_reversed = self.reverseList(head.next)
        head_next.next = head
        head.next = None
        return sub_reversed
