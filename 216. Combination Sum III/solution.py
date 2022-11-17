class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def helper(i, curr, total):
            if len(curr) == k:
                if total == n: return [curr]
                return []
            if i > 9: return []
            # i is to add, not yet added
            # n is total numbers so far
            
            return helper(i+1, curr + [i], total + i) + helper(i+1, curr, total)
            
        
        
        return helper(1, [], 0)
