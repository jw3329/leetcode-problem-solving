class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # stack, make it strict increasing
        # pop if new element is smaller, but make sure to check next elements are enough before popping
        stack = []
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) - 1 + len(nums) - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack
