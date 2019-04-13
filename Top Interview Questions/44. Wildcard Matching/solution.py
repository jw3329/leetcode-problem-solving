class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[len(s)][len(p)] = True
        for i in range(len(p)-1,-1,-1):
            if p[i] != '*': break
            else: dp[len(s)][i] = True
        for i in range(len(s)-1,-1,-1):
            for j in range(len(p)-1,-1,-1):
                if s[i] == p[j] or p[j] == '?': dp[i][j] = dp[i+1][j+1]
                elif p[j] == '*': dp[i][j] = dp[i][j+1] or dp[i+1][j]
                else: dp[i][j] = False
        return dp[0][0]
