class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # set up decreasing stack
        # if curr is less than stack top, then append
        # if bigger, then try to find maximum length of between using binary search
        # since it's decreasing, left most is the biggest
        # track max, then return
        stack = []
        res = 0
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)
            else:
                # make binary search
                left = 0
                right = len(stack) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if nums[stack[mid]] > num:
                        left = mid + 1
                    else:
                        right = mid
                res = max(res, i - stack[left])
        return res
            
