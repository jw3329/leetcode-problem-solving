class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        res = n = len(source)
        G = [set() for _ in range(n)]
        for i, j in allowedSwaps:
            G[i].add(j)
            G[j].add(i)
            
        visited = [False] * n
        
        def dfs(i):
            visited[i] = True
            group.append(i)
            for j in G[i]:
                if not visited[j]:
                    dfs(j)
        
        for i in range(n):
            if visited[i]: continue
            group = []
            dfs(i)
            count1 = collections.Counter(source[j] for j in group)
            count2 = collections.Counter(target[j] for j in group)
            res -= sum((count1 & count2).values())
        return res
