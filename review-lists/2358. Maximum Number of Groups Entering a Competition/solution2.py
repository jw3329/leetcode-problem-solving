class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        left = 0
        right = 1000
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * (mid + 1) > 2 * len(grades):
                right = mid - 1
            else:
                left = mid
        return left
