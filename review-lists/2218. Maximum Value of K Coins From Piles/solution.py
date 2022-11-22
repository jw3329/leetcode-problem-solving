class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # greedy not working
        # backtracking will work, but it will take a lot of time
        
        memo = dict()
        
        def helper(i, k):
            if i == len(piles) or k == 0: return 0
            if (i,k) in memo: return memo[i,k]
            res = helper(i+1, k)
            curr = 0
            for j in range(min(len(piles[i]), k)):
                # do one by one calculation
                curr += piles[i][j]
                res = max(res, curr + helper(i+1, k - j - 1))
            memo[i,k] = res
            return res
        return helper(0, k)
