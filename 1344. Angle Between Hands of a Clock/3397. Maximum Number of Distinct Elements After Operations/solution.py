class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # sort
        # subtract the most
        # put into set
        # increment
        nums.sort()
        res = 0
        last = -sys.maxsize
        for num in nums:
            if last < num - k:
                last = num - k
                res += 1
            elif last < num + k:
                last += 1
                res += 1
        return res
