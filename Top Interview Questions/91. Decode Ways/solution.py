class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        dp = [0 for _ in range(len(s) + 1)]
        
        dp[0] = 1
        dp[1] = 1 if int(s[0]) > 0 else 0
        
        for i in range(2,len(s)+1):
            one_digit = int(s[i-1])
            two_digit = int(s[i-2:i])
            
            if one_digit > 0: dp[i] += dp[i-1]
            if 10 <= two_digit and two_digit <= 26: dp[i] += dp[i-2]
        return dp[len(s)]
