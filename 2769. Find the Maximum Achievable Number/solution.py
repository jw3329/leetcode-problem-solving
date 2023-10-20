class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # making difference with -2 0 2 only
        return num + 2 * t
