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

    def find_min(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def inorderSuccessor(self, root, p):
        if not root:
            return None
        # check value of root and p
        # if p is larger than root, then we don't need to check left side
        # if p is same, then we return left most right
        # if p is less, then potentially it can be root, or value from left
        if root.val < p.val:
            return self.inorderSuccessor(root.right, p)
        if root == p:
            return self.find_min(root.right)
        # left case
        # if left finding is null, then it means no matching or root
        # if left finding is not null, then it means it finds matching from left
        return self.inorderSuccessor(root.left, p) or root
