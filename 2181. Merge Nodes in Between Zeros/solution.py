# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # starting from head
        # you set another pointer, summing up, then modify value, then do same for next
        # last, next is none, then return
        prev = None
        curr = res = head
        sum_val = 0
        curr = curr.next
        while curr:
            while curr.val != 0:
                sum_val += curr.val
                curr = curr.next
            res.val = sum_val
            sum_val = 0
            prev = res
            res = res.next
            curr = curr.next
        prev.next = None
        return head
