class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # using heap, append absolute value subtracting medium with second value
        # heappop k times
        heap = []
        arr.sort()
        # get median
        median = arr[(len(arr) - 1) // 2]
        # append to heap
        for num in arr:
            # should be maximum value first, then second value should be larger
            heapq.heappush(heap, (-abs(num - median), -num))
        # heappop k times
        res = []
        for _ in range(k):
            _, val = heapq.heappop(heap)
            res.append(-val)
        return res
