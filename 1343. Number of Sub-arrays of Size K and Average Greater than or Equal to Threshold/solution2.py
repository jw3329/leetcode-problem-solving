class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        avg = sum(arr[:k])
        res = 0
        for i in range(k-1, len(arr)):
            if avg >= k * threshold:
                res += 1
            if i + 1 < len(arr):
                avg += arr[i+1] - arr[i-k+1]
        return res
