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
            
        def dfs(src, dst, k, curr):
            if src == dst: 
                self.val = curr
                return
            if k == -1: return
            if src not in graph: return
            # do dfs for src to adj vertices
            for adj in graph[src]:
                if curr + adj[1] > self.val: continue
                dfs(adj[0], dst, k-1, curr + adj[1])
            
        self.val = sys.maxsize
        # graph is formed, do dfs
        dfs(src, dst, k, 0)
        return self.val if self.val != sys.maxsize else -1
