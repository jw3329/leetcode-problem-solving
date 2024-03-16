class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # permutation, then maxium of value
        # we need to figure out indexes of occuring
        # calculate number of occurance of indexes
        # then we sort, then grab result
        # we store all indexes
        # count up and down
        count = [0] *len(nums)
        for request in requests:
            count[request[0]] += 1
            if request[1] + 1 < len(nums):
                count[request[1] + 1] -= 1
        for i in range(1, len(nums)):
            count[i] += count[i-1]
        nums.sort()
        count.sort()
        res = 0
        for i in range(len(nums)):
            res += nums[i] * count[i]
        return res % (10**9 + 7)
