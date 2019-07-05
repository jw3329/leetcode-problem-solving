# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildTreeHelper(0,0,len(inorder)-1,preorder,inorder)
    
    def buildTreeHelper(self,preorder_start,inorder_start,inorder_end,preorder,inorder):
        if preorder_start > len(preorder)-1 or inorder_start > inorder_end:
            return None
        
        root = TreeNode(preorder[preorder_start])
        
        inorder_index = inorder.index(root.val)
        root.left = self.buildTreeHelper(preorder_start+1,inorder_start,inorder_index - 1, preorder,inorder)
        root.right = self.buildTreeHelper(preorder_start + inorder_index - inorder_start + 1,
                                         inorder_index + 1, inorder_end, preorder, inorder)
        return root
