class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # using priority queue with dict
        res = dict()
        heap = []
        intervals.sort(key=lambda x: (x[0], x[1]))
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1
        res2 = []
        for q in queries:
            res2.append(res[q])
        return res2
