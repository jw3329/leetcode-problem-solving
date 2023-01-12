class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # -86 -85 -84 ... 13
        min_val = sys.maxsize
        max_val = -sys.maxsize
        curr = 0
        for num in differences:
            curr += num
            min_val = min(min_val, curr)
            max_val = max(max_val, curr)
        lower_bound = max(lower, lower - min_val)
        upper_bound = min(upper, upper - max_val)
        return max(upper_bound - lower_bound + 1, 0)
