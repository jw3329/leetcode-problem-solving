class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        cnt = [i for i in range(10)]
        str_n = str(n)
        
        def dfs(val, sz):
            if sz == 0:
                for i in range(1, 10):
                    if cnt[i] != i and cnt[i] != 0: return 0
                return val if val > n else 0
            for i in range(1, 10):
                if cnt[i] > 0 and cnt[i] <= sz:
                    cnt[i] -= 1
                    res = dfs(10 * val + i, sz - 1)
                    if res != 0: return res
                    cnt[i] += 1
            return 0
        
        val1 = dfs(0, len(str_n))
        if val1: return val1
        return dfs(0, len(str_n) + 1)
