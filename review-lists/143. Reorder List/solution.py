# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next: return
        # we have first half, second half is reversed
        # 1->2 4->3
        # if odd -> pointer is mid
        # even number -> first pointer is at second
        # odd number -> mid
        prev = None
        hare = tortoise = head
        while hare and hare.next:
            hare = hare.next.next
            prev = tortoise
            tortoise = tortoise.next
        prev.next = None
        # now from tortoise, revert the direction
        prev = None
        while tortoise:
            tortoise_next = tortoise.next
            tortoise.next = prev
            prev = tortoise
            tortoise = tortoise_next
        # now prev is pointing to head of reversed
        first = head
        second = prev
        
        # now, operate while both pointer is not null
        while first and second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            if not first_next:
                second.next = second_next
            first = first_next
            second = second_next
