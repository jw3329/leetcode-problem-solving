class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if first of s1 is same, then next s1 with next s3, with s2
        # if first of s2 is same, then next s2 with next s3, with s1
        # if none of them matching, return false
        # i, j for s1 and s2
        if len(s1) + len(s2) != len(s3): return False
        m, n = len(s1), len(s2)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # if s1 is same
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]
        return dp[m][n]
