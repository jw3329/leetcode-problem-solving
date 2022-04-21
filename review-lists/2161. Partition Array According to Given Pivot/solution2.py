class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low = same = 0
        for num in nums:
            if num < pivot:
                low += 1
            elif num == pivot:
                same += 1
        res = [0] * len(nums)
        high = low + same
        same = low
        low = 0
        for num in nums:
            if num < pivot:
                res[low] = num
                low += 1
            elif num == pivot:
                res[same] = num
                same += 1
            else:
                res[high] = num
                high += 1
        return res
            
