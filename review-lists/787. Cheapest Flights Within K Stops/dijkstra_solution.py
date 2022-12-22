class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create the graph
        # do dfs of src to dest
        # return
        
        graph = dict()
        for f in flights:
            if f[0] not in graph:
                graph[f[0]] = []
            graph[f[0]].append((f[1], f[2]))
            
        queue = []
        heapq.heappush(queue, (0, src, k+1))
        while queue:
            cost, curr, stop = heapq.heappop(queue)
            if curr == dst: return cost
            if stop > 0:
                if curr not in graph: continue
                for adj in graph[curr]:
                    heapq.heappush(queue, (cost+adj[1], adj[0], stop-1))
        return -1
            
