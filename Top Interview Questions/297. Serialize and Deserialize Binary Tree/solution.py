# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return str([])
        queue = [root]
        res = []
        while queue:
            curr = queue.pop(0)
            res.append(curr.val if curr else None)
            if not curr: continue
            queue.append(curr.left)
            queue.append(curr.right)
        return str(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        str_list = eval(data)
        if not str_list: return None
        root_val = str_list.pop(0)
        root = TreeNode(root_val)
        queue = [root]
        while queue:
            # print(queue)
            curr = queue.pop(0)
            if not curr: continue
            left_val = str_list.pop(0)
            right_val = str_list.pop(0)
            left = TreeNode(left_val) if left_val != None else None
            right = TreeNode(right_val) if right_val != None else None
            curr.left = left
            curr.right = right
            queue.append(left)
            queue.append(right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
