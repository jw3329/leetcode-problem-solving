class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # do from, to -> value
        # form that up
        from_to_map = dict()
        total_set = set()
        for i in range(len(cost)):
            if original[i] not in from_to_map:
                from_to_map[original[i]] = dict()
            if changed[i] not in from_to_map[original[i]]:
                from_to_map[original[i]][changed[i]] = sys.maxsize
            from_to_map[original[i]][changed[i]] = min(from_to_map[original[i]][changed[i]], cost[i])
            from_to_map[original[i]][original[i]] = 0
            total_set.add(original[i])
            total_set.add(changed[i])
        
        
        # do form up for the cost
        for k in total_set:
            if k not in from_to_map: continue
            for i in total_set:
                if i not in from_to_map: continue
                if k not in from_to_map[i]: continue
                for j in total_set:
                    if j not in from_to_map[k]: continue
                    if j not in from_to_map[i]:
                        from_to_map[i][j] = sys.maxsize
                    from_to_map[i][j] = min(from_to_map[i][j],from_to_map[i][k] + from_to_map[k][j])
        # now calculate
        res = 0
        for i in range(len(source)):
            if source[i] == target[i]: continue
            if source[i] not in from_to_map: return -1
            if target[i] not in from_to_map[source[i]]: return -1
            res += from_to_map[source[i]][target[i]]
        return res
