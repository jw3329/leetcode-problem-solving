class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # 2 3 4 5
        # 1 1 1
        
        # 0 1 5 10 14
        # 1 4 6 4
        # 0 1 1 4 6 6 6
        # 1 0 3 2 0 0
        # 0 0 0 1 2 3
        
        nums.sort()
        return min(b-a for a,b in zip(nums[:4], nums[-4:]))
