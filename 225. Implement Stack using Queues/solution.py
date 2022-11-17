class MyStack:

    def __init__(self):
        # a b c d e f q1
        # f e d c b a q2
        # a b c d e g
        self.queue = deque([])
        self.store = True
        

    def push(self, x: int) -> None:
        # when push is made, use q1 for storing, q2 for popping or peek
        # if q2 is not empty, then store all elements in q2 to q1
        if not self.store:
            # reverse queue
            self.store = True
            self.queue.reverse()
        self.queue.append(x)

    def pop(self) -> int:
        if self.store:
            self.store = False
            self.queue.reverse()
        return self.queue.popleft()
        

    def top(self) -> int:
        if self.store:
            self.store = False
            self.queue.reverse()
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
