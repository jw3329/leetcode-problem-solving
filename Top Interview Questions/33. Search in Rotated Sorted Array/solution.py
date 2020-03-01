from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low,high = 0, len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        
        rotated = low

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            rotated_mid = (mid + rotated) % len(nums)
            
            if nums[rotated_mid] == target: return rotated_mid
            elif nums[rotated_mid] < target: low = mid + 1
            else: high = mid - 1

        return -1



s = Solution()

nums = [4,5,6,7,0,1,2]
target = 0
print(s.search(nums,target))
