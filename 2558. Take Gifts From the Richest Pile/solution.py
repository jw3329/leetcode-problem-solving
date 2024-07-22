class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # heap
        # pop and push
        heap = []
        for gift in gifts:
            heapq.heappush(heap, -gift)
        for _ in range(k):
            popped = -heapq.heappop(heap)
            rooted = int(popped**(1/2))
            heapq.heappush(heap, -rooted)
        return -sum(heap)
