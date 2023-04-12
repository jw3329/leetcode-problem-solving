# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # track left, right, and sum of curr and left, right
        # make it into freq
        # decide highest, if tie, then return any order
        freq = collections.defaultdict(int)
        
        def helper(curr):
            if not curr: return 0
            left_sum = helper(curr.left)
            right_sum = helper(curr.right)
            curr_sum = curr.val + left_sum + right_sum
            freq[curr_sum] += 1
            return curr_sum
        helper(root)
        # iterate map, track max value, then append
        res = []
        max_val = -sys.maxsize
        
        for key in freq:
            val = freq[key]
            if max_val == val:
                res.append(key)
            elif max_val < val:
                max_val = val
                res = [key]
        return res
        
