# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # paindrome condition -> all even or 1 odd
        # iterate from root, to leaf, hold count array, if leaf, then check condition,
        # if condition satisfies, then increment res
        self.res = 0
        count = [0] * 10

        def check():
            one_odd = False
            for freq in count:
                if freq % 2 == 1:
                    if one_odd: return False
                    one_odd = True
            return True
        
        def dfs(root):
            if not root: return
            count[root.val] += 1
            if not root.left and not root.right:
                if check():
                    self.res += 1
                count[root.val] -= 1
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            count[root.val] -= 1


        dfs(root)
        return self.res
