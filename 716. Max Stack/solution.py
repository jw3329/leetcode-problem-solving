class Node:
    def __init__(self, val):
        self.val = val
        self.max_val = val
        self.next = None


class MaxStack:

    def __init__(self):
        self.dummy = Node(0)
        self.head = self.dummy.next
        self.max_prev = None

    def push(self, x):
        new_node = Node(x)
        head = self.dummy.next
        new_node.next = head
        if head:
            sofar_max = head.max_val
            new_node.max_val = max(sofar_max, x)
        else:
            new_node.max_val = x
        self.dummy.next = new_node

    def pop(self):
        head = self.dummy.next
        head_next = head.next
        self.dummy.next = head_next
        return head.val

    def top(self):
        return self.dummy.next.val

    def peekMax(self):
        return self.dummy.next.max_val

    def popMax(self):
        # get maximum so far in the head
        curr = self.dummy.next
        prev = self.dummy
        max_val = curr.max_val
        while curr.val != max_val:
            prev = curr
            curr = curr.next
        # now either curr.next not existing
        curr_next = curr.next
        prev.next = curr_next
        return curr.val


stack = MaxStack()
print(stack.push(5))
print(stack.push(1))
print(stack.push(5))
print(stack.top())
print(stack.popMax())
print(stack.top())
print(stack.peekMax())
print(stack.pop())
print(stack.top())
