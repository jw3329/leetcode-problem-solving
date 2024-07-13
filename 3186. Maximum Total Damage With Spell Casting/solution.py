class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        def helper(index):
            if index >= len(uniques): return 0
            if index in memo: return memo[index]
            # no take first
            skip = helper(index + 1)
            next_index = index + 1
            while next_index < len(uniques) and uniques[next_index] - uniques[index] <= 2:
                next_index += 1
            take = freq[uniques[index]] * uniques[index] + helper(next_index)
            memo[index] = max(take, skip)
            return memo[index]
        
        
        freq = collections.Counter(power)
        uniques = sorted(freq.keys())
        
        memo = dict()
        return helper(0)
