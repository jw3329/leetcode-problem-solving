# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder: return None
        # root --> end of post order
        # left side of root will be left tree, right side will be right
        root = TreeNode(val = postorder[-1])
        root_i = inorder.index(root.val)
        # right side will be length - 1 - root_i
        root.left = self.buildTree(inorder[:root_i], postorder[:root_i])
        root.right = self.buildTree(inorder[root_i+1:], postorder[root_i:-1])
        return root
