class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # store word maximum length
        dp = dict()
        res = 0
        words.sort(key=len)
        for word in words:
            best = 0
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                best = max(best, dp.get(prev, 0) + 1)
            dp[word] = best
            res = max(res, best)
        return res
