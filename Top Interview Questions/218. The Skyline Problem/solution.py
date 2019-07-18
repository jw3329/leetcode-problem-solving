from heapq import *

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        v_lines = {l for b in buildings for l in (b[0],b[1])}
        heap, i, res = [], 0, []
        for vl in sorted(v_lines):
            while i < len(buildings) and buildings[i][0] <= vl:
                heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
                i+=1
            while heap and heap[0][1] <= vl:
                heapq.heappop(heap)
            h = len(heap) and -heap[0][0]
            if not res or res[-1][1]!= h:
                res.append((vl, h))
        return res
