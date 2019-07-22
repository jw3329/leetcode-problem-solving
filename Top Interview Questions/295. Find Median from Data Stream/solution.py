from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = [],[]

    def addNum(self, num: int) -> None:
        small, large = self.heap
        
        heappush(large, num)
        heappush(small, -heappop(large))
        
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self) -> float:
        if len(self.heap[0]) < len(self.heap[1]): return self.heap[1][0]
        return (self.heap[1][0] - self.heap[0][0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
