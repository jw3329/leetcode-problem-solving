class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def dfs(queens, diff, sum):
            if len(queens) == n:
                result.append(queens)
                return
            # p, q
            p = len(queens)
            for q in range(n):
                if q not in queens and p - q not in diff and p + q not in sum:
                    dfs(queens + [q], diff + [p - q], sum + [p + q])
        
        result = []
        # dfs for each queen index
        dfs([],[],[])
        return [['.'*i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in result]
