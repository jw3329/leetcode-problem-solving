class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # first k, then each decrement and increment new, then average
        # keep it into another array, then check for threshhold
        avgs = [0] * (len(arr) - k + 1)
        avgs[0] = sum(arr[:k])
        for i in range(k, len(arr)):
            avgs[i-k+1] = avgs[i-k] - arr[i-k] + arr[i]
        res = 0
        for num in avgs:
            if num >= threshold * k:
                res += 1
        return res
