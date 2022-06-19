class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ess = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        res = 0
        sums = 0
        for es in ess:
            heapq.heappush(heap, es[1])
            sums += es[1]
            if len(heap) > k:
                sums -= heapq.heappop(heap)
            res = max(res, sums * es[0])
        return res % (10 ** 9 + 7)
