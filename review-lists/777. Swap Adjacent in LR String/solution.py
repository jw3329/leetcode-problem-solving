class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start2 = ''
        end2 = ''
        for c in start:
            if c != 'X': start2 += c
        for c in end:
            if c != 'X': end2 += c
        if start2 != end2: return False
        p1 = p2 = 0
        while p1 < len(start) and p2 < len(end):
            while p1 < len(start) and start[p1] == 'X':
                p1 += 1
            while p2 < len(end) and end[p2] == 'X':
                p2 += 1
            # if boths are end, return true
            if p1 == len(start) and p2 == len(end): return True
            if p1 == len(start) or p2 == len(end): return False
            if start[p1] != end[p2]: return False
            if start[p1] == 'L' and p2 > p1: return False
            if start[p1] == 'R' and p2 < p1: return False
            p1 += 1
            p2 += 1
        return True
            
