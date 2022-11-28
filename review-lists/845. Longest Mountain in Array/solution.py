class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        up = [0] * n
        down = [0] * n
        for i in range(n-2,-1,-1):
            if arr[i] > arr[i+1]:
                down[i] = down[i+1] + 1
        res = 0
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                up[i] = up[i-1] + 1
            if up[i] > 0 and down[i] > 0:
                res = max(res, up[i] + down[i] + 1)
        return res
