# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # get all combinations
        # find min
        
        def helper(root, curr):
            if not root:
                return
            if not root.left and not root.right:
                word_set.add(chr(root.val + ord('a')) + curr)
                return
            helper(root.left, chr(root.val + ord('a')) + curr)
            helper(root.right, chr(root.val + ord('a')) + curr)
        
        word_set = set()
        helper(root, '')
        return min(word_set)
