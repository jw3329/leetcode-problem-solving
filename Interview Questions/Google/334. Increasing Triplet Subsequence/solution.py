class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = mid = sys.maxsize
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else: return True
        return False
