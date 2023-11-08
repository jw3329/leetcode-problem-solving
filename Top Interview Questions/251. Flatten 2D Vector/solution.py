class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        # make linkedlist
        self.dummy = Node(0)
        curr = self.dummy
        for vec in vec2d:
            for num in vec:
                # create new node each
                curr.next = Node(num)
                curr = curr.next
        # set up curr pointer
        self.curr = self.dummy

    # @return {int} a next element
    def next(self):
        # Write your code here
        self.curr = self.curr.next
        return self.curr.val
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        return self.curr.next is not None
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
