class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        def helper(a, b, c, aa, bb, cc):
            if a < b:
                return helper (b, a, c, bb, aa, cc)
            # a is bigger than b
            if b < c:
                return helper(a, c, b, aa, cc, bb)
            # a is bigger than b, b is bigger than c
            a_num = min(a, 2)
            if b == 0:
                return aa * a_num
            # now we have base case set up
            # if a - 2 >= b, then we put aa
            b_num = 1 if a - a_num >= b else 0
            return aa * a_num + bb * b_num + helper(a - a_num, b - b_num, c, aa, bb, cc)
    
        return helper(a, b, c, 'a', 'b', 'c')
