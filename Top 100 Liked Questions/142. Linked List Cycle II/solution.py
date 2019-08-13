# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break
        
        if not fast or not fast.next: return None
        
        curr = head
        ptr = slow
        
        while ptr != curr:
            ptr = ptr.next
            curr = curr.next
            
        return curr
