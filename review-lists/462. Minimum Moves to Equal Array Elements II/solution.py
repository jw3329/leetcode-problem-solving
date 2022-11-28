class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # sort, prefix sum, iterate
        nums.sort()
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        # now prefix sum has made
        res = sys.maxsize
        for i in range(len(nums)):
            # 2 * nums[i] * i + prefix[-1] - prefix[i-1] - len(nums)
            temp = 0
            if i > 0:
                temp += nums[i] * i - prefix[i-1]
            temp += prefix[-1] - prefix[i] - (len(nums) - 1 - i) * nums[i]
            res = min(res, temp)
        return res
