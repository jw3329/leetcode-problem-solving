# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        curr = dummy
        node_map = dict()
        while curr:
            prefix += curr.val
            # check if prefix is in node_map
            if prefix not in node_map:
                node_map[prefix] = curr
            else:
                # since it's in node_map, we remove inbetween
                curr = node_map[prefix].next
                p = prefix + curr.val
                while p != prefix:
                    node_map.pop(p)
                    curr = curr.next
                    p += curr.val
                # since we've popped all inbetwee, reset prefix next to curr next
                node_map[prefix].next = curr.next
            curr = curr.next
        return dummy.next

