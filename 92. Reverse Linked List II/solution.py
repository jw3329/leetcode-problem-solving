# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # start and right - left
        # set up prev and after
        # then make reverse, then set up
        curr = head
        prev = None
        for _ in range(left-1):
            prev = curr
            curr = curr.next
        left_part = prev
        # reverse from current
        prev = None
        start = curr
        for _ in range(right-left+1):
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        # 4 -> 3 -> 2
        right_part = curr
        # now concatenate
        if left_part:
            left_part.next = prev
        else:
            # if not left part, it means, head should be prev
            head = prev
        start.next = right_part
        return head
