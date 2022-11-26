class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # set up graph of bidirectional
        # count using set, using sorted
        # count maximum and return
        graph = [[] for _ in range(n)]
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                sorted_set = set()
                # check all connected
                i_adj = graph[i]
                for v in i_adj:
                    sorted_set.add(tuple(sorted([i, v])))
                j_adj = graph[j]
                for v in j_adj:
                    sorted_set.add(tuple(sorted([j, v])))
                res = max(res, len(sorted_set))
        return res
