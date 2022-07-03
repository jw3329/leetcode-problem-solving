class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

class Skiplist:

    def __init__(self):
        self.head = Node(-1)
        

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            while curr.next and curr.next.val < target:
                curr = curr.next
            if curr.next and curr.next.val == target: return True
            curr = curr.down
        return False

    def add(self, num: int) -> None:
        stack = []
        curr = self.head
        while curr:
            while curr.next and curr.next.val < num:
                curr = curr.next
            stack.append(curr)
            curr = curr.down
        insert = True
        down = None
        while insert and stack:
            curr = stack.pop()
            node = Node(num)
            node.next = curr.next
            node.down = down
            curr.next = node
            down = curr.next
            insert = random.randint(0, 1) == 1
        if insert: 
            head = Node(-1)
            head.down = self.head
            self.head = head

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            while curr.next and curr.next.val < num:
                curr = curr.next
            if curr.next and curr.next.val == num:
                found = True
                curr.next = curr.next.next
            curr = curr.down
        return found
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
