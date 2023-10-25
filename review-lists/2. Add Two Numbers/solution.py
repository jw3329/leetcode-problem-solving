# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add once more, with carrying
        prev = None
        h1 = l1
        h2 = l2
        # keeping track if none or not
        carry = False
        while h1 and h2:
            added = h1.val + h2.val + carry
            carry = False
            if added >= 10:
                carry = True
                added -= 10
            h1.val = added
            prev = h1
            h1 = h1.next
            h2 = h2.next
        if not h2:
            if not h1 and carry:
                prev.next = ListNode(1)
                return l1
            # now we have h1 available
            while h1:
                added = h1.val + carry
                carry = False
                if added >= 10:
                    carry = True
                    added -= 10
                h1.val = added
                prev = h1
                h1 = h1.next
            if not h1 and carry:
                prev.next = ListNode(1)
                return l1
        # assume h2 is the one
        prev.next = h2
        while h2:
            added = h2.val + carry
            carry = False
            if added >= 10:
                carry = True
                added -= 10
            h2.val = added
            prev = h2
            h2 = h2.next
        if not h2 and carry:
            prev.next = ListNode(1)
            return l1
        return l1
