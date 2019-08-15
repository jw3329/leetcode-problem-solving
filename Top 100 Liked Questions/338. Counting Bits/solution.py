class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        max_power = 1
        prev_max = 1
        for i in range(1,num+1):
            if max_power == i:
                prev_max = max_power
                max_power *= 2
            dp[i] = 1 + dp[i-prev_max]
        return dp
