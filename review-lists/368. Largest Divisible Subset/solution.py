class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        prev = [0] * len(nums)
        nums.sort()
        max_val = 0
        index = -1
        for i in range(len(nums)):
            l[i] = 1
            prev[i] = -1
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0 and l[j] + 1 > l[i]:
                    l[i] = l[j] + 1
                    prev[i] = j
            if l[i] > max_val:
                max_val = l[i]
                index = i
        res = []
        while index != -1:
            res.append(nums[index])
            index = prev[index]
        return res
