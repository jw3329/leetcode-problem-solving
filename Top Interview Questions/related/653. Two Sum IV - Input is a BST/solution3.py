# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # binary search, assuming root is included
        # gotta pick one element, and find into other way
        return self.find(root, root, k)
    
    def find(self, root, curr, k):
        if not curr: return False
        return self.search(root, curr, k - curr.val) or self.find(root, curr.left, k) or self.find(root, curr.right, k)
    
    def search(self, root, curr, left):
        if not root: return False
        # now we search left overs, curr is already defined, we move root
        if left == root.val:
            if root == curr: return False
            return True
        if root.val < left: return self.search(root.right, curr, left)
        return self.search(root.left, curr, left)
