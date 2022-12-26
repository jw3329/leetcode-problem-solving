class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        # sum first, 
        # s + x * limit = goal
        # goal - s 
        # if > 0 -> x needs to be ceil
        # if < 0 -> 
        val = goal - sum(nums)
        return math.ceil(abs(val / limit))
