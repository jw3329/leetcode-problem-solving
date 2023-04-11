class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # iterate num, check if it's same with groups[i], if same, then 
        # update j, 
        i = j = 0
        while j < len(nums) and i < len(groups):
            k = j
            match = True
            for num in groups[i]:
                if k < len(nums) and num == nums[k]:
                    k += 1
                else:
                    match = False
                    break 
            if match:
                i += 1
                j = k
            else:
                j += 1
        return i == len(groups)
