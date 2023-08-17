class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # 4 0 1 0
        count_map = dict()
        res = 0
        for i in range(len(nums)):
            val = nums[i] - i
            if val not in count_map:
                count_map[val] = 0
            res += i - count_map[val]
            count_map[val] += 1
        return res
