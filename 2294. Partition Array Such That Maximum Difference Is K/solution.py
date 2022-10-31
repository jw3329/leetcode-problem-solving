class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        mx = mn = nums[0]
        for num in nums:
            mx = max(mx, num)
            mn = min(mn, num)
            if mx - mn > k:
                res += 1
                mx = mn = num
        return res
