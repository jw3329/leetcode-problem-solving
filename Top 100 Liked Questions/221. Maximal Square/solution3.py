class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        dp = [0] * (len(matrix[0]) + 1)
        max_length = 0
        prev = 0
        for i in range(1,len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    max_length = max(max_length, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return max_length * max_length
