# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            head_next = head.next
            head.next = prev
            prev = head
            head = head_next
        return prev
