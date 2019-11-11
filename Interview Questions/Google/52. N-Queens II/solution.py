class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, diff, sum):
            if len(queens) == n:
                self.result += 1
                return
            # p, q
            p = len(queens)
            for q in range(n):
                if q not in queens and p - q not in diff and p + q not in sum:
                    dfs(queens + [q], diff + [p - q], sum + [p + q])
        
        self.result = 0
        # dfs for each queen index
        dfs([],[],[])
        return self.result
