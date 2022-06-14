class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # sort edges by 0, and 1
        # create graph, node -> adjs
        # for node in adj, append it, and dfs into it
        res = [[] for _ in range(n)]
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
        
        def dfs(node, curr, visited):
            for neighbor in graph[node]:
                if visited[neighbor]: continue
                visited[neighbor] = True
                res[neighbor].append(curr)
                dfs(neighbor, curr, visited)
        
        for i in range(n):
            visited = [False] * n
            dfs(i,i, visited)
        return res
