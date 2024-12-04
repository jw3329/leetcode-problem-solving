class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # find min and max
        # if each side, then we just do left + right
        # if one side, then max of those
        min_val = sys.maxsize
        max_val = -sys.maxsize
        min_index = -1
        max_index = -1
        for i, num in enumerate(nums):
            if num < min_val:
                min_val = num
                min_index = i
            if num > max_val:
                max_val = num
                max_index = i
        # now min and max set up done
        # check side by side
        left = min_index
        right = max_index
        if left > right:
            left, right = right, left
        # now left and right set up
        # check side by side
        # left + 1  x-1 -> x - 1 - left
        return min(right+1, len(nums)-left,len(nums) - right + left + 1)
        
