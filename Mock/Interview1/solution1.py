class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if not A and not B: return True
        for i in range(len(B)):
            if A == B[i:] + B[:i]: return True
        return False
