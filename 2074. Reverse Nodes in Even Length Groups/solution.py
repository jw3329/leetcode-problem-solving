# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(curr, num):
            prev = None
            count = 0
            tail = curr
            while curr and count < num:
                curr_next = curr.next
                curr.next = prev
                prev = curr
                curr = curr_next
                count += 1
            return prev, tail

        # check num of nodes for each group
        # if found even, then reverse it
        target = 1
        curr = head
        prev = None
        while curr:
            # check count
            count = 0
            hare = curr
            hare_prev = None
            while count < target and hare:
                hare_prev = hare
                hare = hare.next
                count += 1
            # now hare is either at the start of second
            # or none
            # check count is even or not
            if count % 2 == 0:
                # then reverse, then return head and tail
                r_h, r_t = reverse(curr, count)
                prev.next = r_h
                r_t.next = hare
                prev = r_t
                curr = hare
            else:                    
                # now update
                prev = hare_prev
                curr = hare
            target += 1
        return head

