class Node:
    
    def __init__(self, val = 0, min_val = sys.maxsize, next = None):
        self.val = val
        self.min_val = min_val
        self.next = next

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(self.head.min_val, val), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
