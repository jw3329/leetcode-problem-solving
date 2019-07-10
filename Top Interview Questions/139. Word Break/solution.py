class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # if not s: return True
        # for word in wordDict:
        #     if len(s) >= len(word) and s[:len(word)] == word:
        #         if self.wordBreak(s[len(word):],wordDict): return True
        # return False
        
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        
        for i in range(1,len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]
