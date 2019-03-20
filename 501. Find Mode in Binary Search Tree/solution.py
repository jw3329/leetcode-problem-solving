# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        dic = {}
        self.findModeHelper(root,dic)
        sortedItem = sorted(dic.items(), key=lambda x : x[1], reverse=True)
        res = []
        val = sortedItem[0][1]
        i = 0
        while i < len(sortedItem) and sortedItem[i][1] == val:
            res.append(sortedItem[i][0])
            i += 1
        return res
    
    def findModeHelper(self,root,dic):
        if not root: return
        self.findModeHelper(root.left,dic)
        self.findModeHelper(root.right,dic)
        if root.val not in dic: dic[root.val] = 1
        else: dic[root.val] += 1
