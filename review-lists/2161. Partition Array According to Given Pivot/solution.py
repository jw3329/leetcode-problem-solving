class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # find pivot index, and switch to last element
        # set as pivot for last, make changes
        index = nums.index(pivot)
        left = 0
        same_count = 0
        bigger_list = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == pivot: same_count += 1
            else:
                bigger_list.append(nums[i])
        return nums[:left] + [pivot] * same_count + bigger_list
