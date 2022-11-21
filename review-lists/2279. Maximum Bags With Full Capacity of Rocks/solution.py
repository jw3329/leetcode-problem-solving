class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # need to determine if to put the rock in the first bag or not
        # it will be too time consuming, put one by one, then do dfs
        # do subtraction from capacity to rocks, then do heap push,
        # subtract amount of aditional rocks by remaining of heap, do until no more rocks available, then return
        heap = []
        for i in range(len(capacity)):
            # push into heap of subtraction
            heapq.heappush(heap, capacity[i] - rocks[i])
        res = 0
        while heap and additionalRocks > 0:
            # subtract additional rock of first pop
            popped = heapq.heappop(heap)
            additionalRocks -= popped
            if additionalRocks >= 0:
                res += 1
        return res
