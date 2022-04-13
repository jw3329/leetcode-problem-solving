class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # set up union find
        n = len(source)
        parents = [i for i in range(n)]
        
        def find(i):
            if parents[i] == i: return i
            parents[i] = find(parents[i])
            return parents[i]
        
        
        # make union of all swaps
        for i, j in allowedSwaps:
            i_par = find(i)
            j_par = find(j)
            parents[i_par] = j_par
            
        # collect index of same group, compare diff and store into res
        group_map = dict()
        for i in range(n):
            par = find(i)
            if par not in group_map:
                group_map[par] = dict()
            num = source[i]
            if num not in group_map[par]:
                group_map[par][num] = 0
            group_map[par][num] += 1
        res = 0
        # now, decrement for each target found on same group
        for i in range(n):
            par = find(i)
            num = target[i]
            group = group_map[par]
            if num not in group or group[num] == 0:
                res += 1
            else: group[num] -= 1
        
        return res
        
