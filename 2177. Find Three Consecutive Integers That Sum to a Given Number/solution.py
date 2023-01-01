class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # n-1 n n+1 -> 3n
        if num % 3 != 0: return []
        mid = num // 3
        return [mid-1, mid, mid+1]
