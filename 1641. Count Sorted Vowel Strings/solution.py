class Solution:
    def countVowelStrings(self, n: int) -> int:
        # aeiou -> 5 4 3 2 1 ->
        # 3 -> aaa aae aai aao aau -> 
        # 5 + n - 1 C n ->
        # 5 + n - 1 ! / n ! / 
        
        memo = dict()
        
        def fact(n):
            if n == 0: return 1
            if n in memo: return memo[n]
            memo[n] = n * fact(n-1)
            return memo[n]
        
        def comb(a, b):
            return fact(a) // fact(b) // fact(a-b)
        
        return comb(5 + n - 1, n)
