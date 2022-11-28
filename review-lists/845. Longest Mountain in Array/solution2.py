class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        up = down = res = 0
        for i in range(1, len(arr)):
            # reset if not mountain
            if down > 0 and arr[i-1] < arr[i] or arr[i-1] == arr[i]:
                up = down = 0
            if arr[i-1] > arr[i]:
                down += 1
            if arr[i-1] < arr[i]:
                up += 1
            if up > 0 and down > 0 and up + down + 1 > res:
                res = up + down + 1
        return res
