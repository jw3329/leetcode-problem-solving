# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # level will be there
        # total -> 2 ** n - 1
        
        # grab height h
        # make 2**h - 1
        # put middle
        # do recursive 
        
        def height(root):
            if not root: return 0
            return 1 + max(height(root.left), height(root.right))
        
        def mark(root, left, right, level):
            if not root: return
            mid = left + (right - left) // 2
            res[level - 1][mid] = f'{root.val}'
            mark(root.left, left, mid-1, level+1)
            mark(root.right,mid+1,right, level+1)
        
        h = height(root)
        m = h
        n = 2 ** h - 1
        res = [[''] * n for _ in range(m)]
        
        mark(root,0, n, 1)
        
        return res
