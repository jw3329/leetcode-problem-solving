class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # as you have more degrees for each node, you should put label bigger
        # set up graph first bidirectional
        # heap push length of degrees, while popping, multiply with and add to res
        graph = collections.defaultdict(list)
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        heap = []
        for node in graph:
            heapq.heappush(heap, (-len(graph[node])))
        res = 0
        while heap:
            degrees = -heapq.heappop(heap)
            res += degrees * n
            n -= 1
        return res
