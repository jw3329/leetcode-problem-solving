class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if not (i == 0 or nums[i] != nums[i-1]): continue
            for j in range(i+1,len(nums)-2):
                if not (j == i+1 or nums[j] != nums[j-1]): continue
                low = j+1
                high = len(nums)-1
                while low < high:
                    test_sum = nums[i] + nums[j] + nums[low] + nums[high]
                    if test_sum == target:
                        res.append([nums[i],nums[j],nums[low],nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low-1]: low += 1
                        while low < high and nums[high] == nums[high+1]: high -= 1

                    elif test_sum < target:
                        low += 1
                    else:
                        high -= 1
        return res
