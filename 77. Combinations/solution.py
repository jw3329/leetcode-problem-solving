class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nCk -> n-1Ck + n-1Ck-1
        if n == k: return [[i+1 for i in range(n)]]
        if k == 1: return [[i+1] for i in range(n)]
        return self.combine(n-1, k) + [sub + [n] for sub in self.combine(n-1, k-1)]
