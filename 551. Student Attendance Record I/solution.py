class Solution:
    def checkRecord(self, s: str) -> bool:
        # a count should be less than 2
        # if not l, reset late count to 0
        a = 0
        l = 0
        for c in s:
            if c == 'L':
                l += 1
                if l == 3:
                    return False
            else:
                l = 0
                if c == 'A':
                    a += 1
                    if a == 2: return False
        return True
