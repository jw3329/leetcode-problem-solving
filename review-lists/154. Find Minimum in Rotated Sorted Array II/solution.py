class Solution:
    def findMin(self, nums: List[int]) -> int:
        # mid compare with right
        # if right is bigger than mid, it means, it has not been rotated, so search left
        # if right is less than mid, it means, it has been rotated, so search right
        # right is same, min can be left side or right side
        # if we reduce size, because it has same on the left, it will still be findable
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
