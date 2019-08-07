class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = {}
        _sum,res = 0, 0
        presum[0] = 1
        for num in nums:
            _sum += num
            if _sum - k in presum:
                res += presum[_sum - k]
            if _sum not in presum: presum[_sum] = 0
            presum[_sum] += 1
        return res
