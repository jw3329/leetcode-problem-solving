# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def to_string(node):
            res = ''
            while node:
                res += str(node.val)
                node = node.next
            return res
        
        
        l1_str = to_string(l1)
        l2_str = to_string(l2)
        
        result = str(int(l1_str[::-1]) + int(l2_str[::-1]))
        
        head = ListNode(0)
        cur = head
        
        for c in result[::-1]:
            cur.next = ListNode(int(c))
            cur = cur.next
        return head.next
    
