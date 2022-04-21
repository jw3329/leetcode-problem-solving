class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        h2p = [[] for _ in range(41)]
        for i in range(n):
            for hat in hats[i]:
                h2p[hat].append(i)
        # dp[i][j] --> i -> hat, j --> bitmask of assigned people, 1024
        dp = [[-1] * 1024 for _ in range(41)]
        return self.dfs(h2p, (1 << n) - 1, 1, 0, dp)
    
    def dfs(self, h2p, all_mask, hat, assigned_people, dp):
        if assigned_people == all_mask: return 1
        if hat > 40: return 0
        if dp[hat][assigned_people] != -1: return dp[hat][assigned_people]
        # should consider wear + non-wear
        ans = self.dfs(h2p, all_mask, hat+1, assigned_people, dp) # not wearing
        for p in h2p[hat]:
            if (assigned_people >> p) & 1: continue
            ans += self.dfs(h2p, all_mask, hat+1, assigned_people | (1 << p), dp)
            ans %= (10**9 + 7)
        dp[hat][assigned_people] = ans
        return ans
