class FreqStack:

    def __init__(self):
        # key --> number, value = list of numbers
        self.map = {}
        self.index_map = collections.Counter()

    def push(self, x: int) -> None:
        self.index_map[x] += 1
        if self.index_map[x] not in self.map:
            self.map[self.index_map[x]] = []
        self.map[self.index_map[x]].append(x)
        # self.map[self.index_map[x]-1].remove(x)

    def pop(self) -> int:
        largest = list(self.map.keys())[-1]
        res = self.map[largest].pop()
        self.index_map[res] -= 1
        if not self.map[largest]: self.map.pop(largest)
        return res
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
