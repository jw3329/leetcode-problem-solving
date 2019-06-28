# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        s = []

        cur = root

        while cur or s:
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop()
            res.append(cur.val)
            cur = cur.right
        return res


root = TreeNode(1)

root.right = TreeNode(2)

root.right.left = TreeNode(3)

print(Solution().inorderTraversal(root))
