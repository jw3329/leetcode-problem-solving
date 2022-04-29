class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_dict = collections.Counter(nums)
        res = 0
        for num in num_dict:
            if num == k - num:
                # if it's same, then we can have total // 2
                res += num_dict[num] // 2
            elif k - num in num_dict and num_dict[k-num] > 0:
                # since we know curr num is in dict, we should check if k - num is in dict,
                # if it's in dict, and has more than zero count, we are operating same
                min_count = min(num_dict[num], num_dict[k-num])
                res += min_count
                num_dict[k-num] -= min_count
                num_dict[num] -= min_count
        return res
