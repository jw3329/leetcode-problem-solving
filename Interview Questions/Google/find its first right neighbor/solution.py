class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.parent = None


def form_parent_pointer(root):

    if not root: return

    form_parent_pointer(root.left)
    form_parent_pointer(root.right)

    if root.left:
        root.left.parent = root
    if root.right:
        root.right.parent = root


def first_right_node(node):
    if not node: return None
    curr = node.parent
    if curr.right and curr.right != node: return curr.right
    while True:
        curr_first_right = first_right_node(curr)
        if not curr_first_right: return None
        if curr_first_right.left: return curr_first_right.left
        if curr_first_right.right: return curr_first_right.right
        curr = curr_first_right
    return first_right_node(node)


root = TreeNode(0)

root.left = TreeNode(1)

root.left.left = TreeNode(3)

root.right = TreeNode(2)

root.right.right = TreeNode(4)

form_parent_pointer(root)

print(first_right_node(root.left.left).val)
