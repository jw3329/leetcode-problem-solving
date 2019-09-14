import sys

def num_squares(n):
    if n == 0: return 0
    min_val = sys.maxsize

    for i in range(1,int(n**(1/2)) + 1):
        min_val = min(min_val, num_squares(n - i**2) + 1)
    return min_val

def num_squares_dp(n):
    
    dp = [0] * (n+1)
    for i in range(1,(n+1)):
        min_val = sys.maxsize
        for j in range(1,int(i**(1/2)) + 1):
            min_val = min(min_val, dp[i - j**2] + 1)
        dp[i] = min_val
    return dp[n]
        




print(num_squares_dp(7334))
