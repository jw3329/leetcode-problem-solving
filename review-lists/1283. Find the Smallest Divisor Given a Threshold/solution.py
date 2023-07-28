class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = 10**6
        while left < right:
            mid = left + (right - left) // 2
            s = 0
            for num in nums:
                s += (num + mid - 1) // mid
            # if sum is less than t, then we make right = mid
            # if sum is bigger, then left = mid + 1
            if s > threshold:
                left = mid + 1
            else:
                right = mid
        return left
