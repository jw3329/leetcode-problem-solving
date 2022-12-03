class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.res = 0
        graph = collections.defaultdict(list)
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        
        def dfs(i, prev, people=1):
            for x in graph[i]:
                if x == prev: continue
                people += dfs(x, i)
            self.res += math.ceil(people / seats) if i != 0 else 0
            return people
        
        
        dfs(0, 0)
        return self.res
