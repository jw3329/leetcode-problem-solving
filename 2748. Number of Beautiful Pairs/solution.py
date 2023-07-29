class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        
        def gcd(i, j):
            if j == 0: return i
            return gcd(j, i % j)
        
        # memoize each
        memo = [[False] * 10 for _ in range(10)]
        for i in range(10):
            for j in range(i, 10):
                memo[i][j] = gcd(i, j) == 1
        
        # bruteforce -> two iterate, if gcd is 1, then oincrement
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s1 = str(nums[i])
                s2 = str(nums[j])
                # front
                d1 = int(s1[0])
                d2 = int(s2[-1])
                max_num = max(d1, d2)
                min_num = min(d1, d2)
                if memo[min_num][max_num]: res += 1
        return res
        
