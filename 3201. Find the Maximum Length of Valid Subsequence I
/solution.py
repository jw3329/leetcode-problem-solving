class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = nums[0] % 2
        odd = even = both = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            if c == num % 2:
                c = 1 - c
                both += 1
        return max(odd, even, both)
