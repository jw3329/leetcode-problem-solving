class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # if target is even, res += 1, maxDouble -= 1, target /= 2
        # if target is odd, res += 1 , target -= 1 until target = 1
        res = 0
        while target != 1:
            if maxDoubles == 0:
                res += target - 1
                target = 1
            else:
                if target % 2 == 0 and maxDoubles > 0:
                    maxDoubles -= 1
                    target //= 2
                else:
                    target -= 1
                res += 1
        return res
