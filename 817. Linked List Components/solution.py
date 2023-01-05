# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # make into set
        # dfs from head, checking all then make next
        # next, increment value, then dfs wise,
        # return
        num_set = set(nums)
        curr = head
        res = 0
        
        def dfs(curr):
            while curr and curr.val in num_set:
                curr = curr.next
            return curr
        
        while curr:
            if curr.val not in num_set:
                curr = curr.next
            else:
                res += 1
                curr = dfs(curr)
        return res
