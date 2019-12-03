class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square_set = set()
        i = 0
        while i * i <= c:
            square_set.add(i*i)
            i += 1
            
        for square in square_set:
            if c - square in square_set: return True
        return False
