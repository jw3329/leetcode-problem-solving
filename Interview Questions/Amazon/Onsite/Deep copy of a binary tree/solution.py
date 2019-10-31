
class TreeNode:
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def inorder_traversal(root):
    if not root: return []
    return inorder_traversal(root.left) + [(root.val, id(root))] + inorder_traversal(root.right)


def deep_copy(root):
    
    if not root: return None

    left_copy = deep_copy(root.left)
    right_copy = deep_copy(root.right)

    new_root = TreeNode(root.val)
    new_root.left = left_copy
    new_root.right = right_copy

    return new_root








if __name__ == '__main__':
    
    root = TreeNode(0)

    root.left = TreeNode(1)

    root.right = TreeNode(2)

    root.left.right = TreeNode(3)

    root.right.left = TreeNode(4)

    root.right.right = TreeNode(5)

    print(inorder_traversal(root))

    print(inorder_traversal(deep_copy(root)))
