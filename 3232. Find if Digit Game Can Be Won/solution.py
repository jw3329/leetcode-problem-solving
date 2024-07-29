class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        # if same, then false
        # if not same, then true
        single = 0
        double = 0
        for num in nums:
            if num >= 10:
                double += num
            else:
                single += num
        return single != double
