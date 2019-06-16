class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.traversed = False
        self.parent = None

    def addLeftNode(self, node):
        self.left = node
        node.parent = self

    def addRightNode(self, node):
        self.right = node
        node.parent = self

    def isLeaf(self):
        return not self.left and not self.right


def getSomeOfLeaves(root):
    res = 0
    cur = root
    while not root.traversed:
        if not cur:
            cur = cur.parent
        elif cur.isLeaf():
            cur.traversed = True
            res += cur.value
            cur = cur.parent
        elif cur.left and not cur.left.traversed:
            cur = cur.left
        elif cur.right and not cur.right.traversed:
            cur = cur.right
        elif (cur.left and cur.left.traversed or cur.right and cur.right.traversed):
            cur.traversed = True
            cur = cur.parent
    return res


root = Node(10)

left_root = Node(5)
left_root.addLeftNode(Node(1))
left_root.addRightNode(Node(2))

right_node = Node(7)
right_node.addLeftNode(Node(3))
right_node.addRightNode(Node(4))

root.addLeftNode(left_root)
root.addRightNode(right_node)

print(getSomeOfLeaves(root))
