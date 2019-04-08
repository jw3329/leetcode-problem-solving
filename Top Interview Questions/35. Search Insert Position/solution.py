class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high - low) // 2 + low
            if nums[mid] == target: return mid
            elif nums[mid] > target: high = mid - 1
            else: low = mid + 1
        return high + 1
