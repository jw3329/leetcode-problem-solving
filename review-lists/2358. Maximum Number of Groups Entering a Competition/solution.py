class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        k = 0
        n = len(grades)
        while n >= k + 1:
            k += 1
            n -= k
        return k
