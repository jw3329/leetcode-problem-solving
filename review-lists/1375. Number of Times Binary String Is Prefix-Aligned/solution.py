class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # find out steps, that includes all sorted
        # track current maximum, if i+1 == maximum, add to prefix
        max_val = -1
        res = 0
        for i, flip in enumerate(flips):
            max_val = max(max_val, flip)
            if i + 1 == max_val:
                res += 1
        return res
