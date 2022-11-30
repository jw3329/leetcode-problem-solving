class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # mod first
        # track dp for 0 and 1, dp_zero[i] -> num of sub array starting at i with sum zero
        # dp_one[i] -> num of sub array starting at i with sum one
        # if odd -> dp_zero[i] -> dp_one[i+1], dp_one[i] -> 1 + dp_zero[i+1]
        # if even -> dp_one[i] -> dp_one[i+1], dp_zero[i] -> 1 + dp_zero[i+1]
        # sum up then
        for i in range(len(arr)):
            arr[i] %= 2
        dp_zero = [0] * len(arr)
        dp_one = [0] * len(arr)
        mod = 10 ** 9 + 7
        if arr[-1] == 0:
            dp_zero[-1] = 1
        else:
            dp_one[-1] = 1
        # now, iterate, and make calculation
        for i in range(len(arr)-2,-1,-1):
            if arr[i] == 0:
                dp_one[i] = dp_one[i+1]
                dp_zero[i] = (dp_zero[i+1] + 1) % mod
            else:
                dp_one[i] = (dp_zero[i+1] + 1) % mod
                dp_zero[i] = dp_one[i+1]
        # now, sum up
        res = 0
        for elem in dp_one:
            res = (res + elem) % mod
        return res
