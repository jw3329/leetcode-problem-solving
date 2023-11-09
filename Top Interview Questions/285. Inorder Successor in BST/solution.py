"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        # since it's bst
        # check the value for p
        # if p is less than root, then we find left side of it
        # if p is same for root val, find right min value
        # if p is larger than root val, then it should be found on the right side

        def find_min(curr):
            while curr and curr.left:
                curr = curr.left
            return curr

        def helper(root):
            if not root: return None
            # check value
            if root.val < p.val:
                return helper(root.right)
            # check left
            if root.val > p.val:
                left = helper(root.left)
                return left or root
            # now same case, we find next min
            return find_min(root.right)


        return helper(root)

