class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        divisor = 2 * k + 1
        if len(nums) < divisor: return res
        curr = sum(nums[:divisor])
        res[k] = curr // divisor
        for i in range(k+1, len(nums) - k):
            curr += nums[i+k] - nums[i-k-1]
            res[i] = curr // divisor
        return res
