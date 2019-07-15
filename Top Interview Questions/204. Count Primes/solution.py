class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        
        not_prime = [False for _ in range(n)]
        
        not_prime[0] = True
        not_prime[1] = True
        
        for i in range(2,int(n**(1/2))+1):
            if not not_prime[i]:
                j = 2
                while i * j < n:
                    not_prime[i*j] = True
                    j += 1
        
        count = 0
        
        for i in range(2,len(not_prime)):
            if not not_prime[i]: count += 1
                
        return count
                    
