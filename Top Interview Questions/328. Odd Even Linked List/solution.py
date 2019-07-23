# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return None
        first = head
        second = head.next
        curr = head
        while curr and curr.next:
            curr_next = curr.next
            curr.next = curr.next.next
            curr = curr_next
        while first.next: first = first.next
        first.next = second
        return head
