class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        def gcd(i,j):
            if j == 0: return i
            return gcd(j, i % j)
        
        res = []
        for i in range(1, n):
            for j in range(i+1, n+1):
                if gcd(i,j) != 1: continue
                res.append(f'{i}/{j}')
        return res
