class LRUCache(object):
    
    class DLinkedNode:
        key = None
        value = None
        next = None
        prev = None
        
    def add_node(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def remove_node(self,node):
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        
        
    def move_to_head(self,node):
        
        self.remove_node(node)
        self.add_node(node)
        
    def pop_tail(self):
        last = self.tail.prev
        self.remove_node(last)
        return last
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.head = self.DLinkedNode()
        self.tail = self.DLinkedNode()
        self.head.prev = None
        self.head.next = self.tail
        self.tail.next = None
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache: return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key not in self.cache:
            new_node = self.DLinkedNode()
            new_node.key = key
            new_node.value = value
            self.cache[key] = new_node
            self.add_node(new_node)
            self.count += 1
            if self.count > self.capacity:
                tail = self.pop_tail()
                self.cache.pop(tail.key)
                self.count -= 1
        else:
            self.cache[key].value = value
            self.move_to_head(self.cache[key])
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
