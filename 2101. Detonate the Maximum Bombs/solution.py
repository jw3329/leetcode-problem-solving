class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # one bomb, then multi,
        # check all, but we have duplicate, memoize that
        graph = collections.defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                # make graph if it's reachable
                if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2:
                    graph[i].append(j)
                    
        def dfs(i, visited):
            if i in visited: return 0
            visited.add(i)
            res = 1
            for j in graph[i]:
                res += dfs(j, visited)
            return res
        
        # track dfs and find max val
        res = 0
        for i in range(n):
            visited = set()
            res = max(res, dfs(i, visited))
        return res
        
