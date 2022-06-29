class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # worst -> concat
        # aabc cab -> caabc
        # if same, put letter,
        # if not same, each put, then redo func
        # return minimum
        # dp[i][j] -> length i and length j
        # if same, dp[i][j] = dp[i-1][j-1] + letter
        # if not same, dp[i][j] => minimum length, then do
        # return length of it
        
        def lcs(str1, str2):
            dp = [[''] * (len(str2) + 1) for _ in range(len(str1) + 1)]
            for i in range(len(str1)):
                for j in range(len(str2)):
                    if str1[i] == str2[j]:
                        dp[i+1][j+1] = dp[i][j] + str1[i]
                    else:
                        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)
            return dp[-1][-1]
        
        res = ''
        i = 0
        j = 0
        for c in lcs(str1, str2):
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        
        return res + str1[i:] + str2[j:]
