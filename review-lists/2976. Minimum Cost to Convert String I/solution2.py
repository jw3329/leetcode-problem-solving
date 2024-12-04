import sys
from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # do from, to -> value
        # form that up
        from_to_map = dict()
        total_set = set()
        for i in range(len(cost)):
            if original[i] not in from_to_map:
                from_to_map[original[i]] = dict()
            if changed[i] not in from_to_map[original[i]]:
                from_to_map[original[i]][changed[i]] = sys.maxsize
            from_to_map[original[i]][changed[i]] = min(
                from_to_map[original[i]][changed[i]], cost[i]
            )
            from_to_map[original[i]][original[i]] = 0
            total_set.add(original[i])
            total_set.add(changed[i])

        # now generate the costs

        def dfs(u, v, visited):
            if u == v:
                return 0
            if u not in from_to_map:
                return sys.maxsize
            if u in visited:
                return sys.maxsize
            if u in costs and v in costs[u]:
                return costs[u][v]
            res = sys.maxsize
            visited.add(u)
            for w in from_to_map[u]:
                res = min(res, from_to_map[u][w] + dfs(w, v, visited))
            visited.remove(u)
            return res

        costs = dict()
        for u in total_set:
            if u not in costs:
                costs[u] = dict()
            for v in total_set:
                visited = set()
                costs[u][v] = dfs(u, v, visited)

        print(costs)

        # now calculate
        res = 0
        for i in range(len(source)):
            if source[i] not in costs:
                return -1
            res += costs[source[i]][target[i]]
        return res


s = Solution()
source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
print(s.minimumCost(source, target, original, changed, cost))
