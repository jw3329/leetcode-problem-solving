# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a,b):
            if b == 0: return a
            return gcd(b, a % b)
        
        def merge(head, temp):
            curr = head
            i = 0
            while i < len(temp):
                curr_next = curr.next
                curr.next = ListNode(temp[i])
                curr.next.next = curr_next
                curr = curr_next
                i += 1
            return head
        
        # calculate first then insert
        first = head.next
        second = head
        temp = []
        while first:
            temp.append(gcd(first.val, second.val))
            first = first.next
            second = second.next
        return merge(head, temp)
