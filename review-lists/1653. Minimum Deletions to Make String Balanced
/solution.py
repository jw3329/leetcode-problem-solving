class Solution:
    def minimumDeletions(self, s: str) -> int:
        # dp[i] -> num of removals total from substr s[:i]
        dp = [0] * (len(s) + 1)
        bcount = 0
        for i in range(len(s)):
            if s[i] == 'a':
                # check if removal or not
                # 1. remove -> when prev is form of a..ab..b -> dp[i] + 1
                # 2. keep -> when prev is form of a..a -> if prev is a then dp[i] else 1 + dp[i]
                dp[i+1] = min(1 + dp[i], bcount)
            else:
                bcount += 1
                dp[i+1] = dp[i]
        return dp[len(s)]
