class Solution:
    def primePalindrome(self, N: int) -> int:
        if 8 <= N <= 11: return 11
        
        def is_prime(x):
            if x < 2 or x % 2 == 0: return x == 2
            for i in range(3,int(x**0.5)+1,2):
                if x % i == 0: return False
            return True
        
        for i in range(10**(len(str(N)) // 2), 10**5):
            y = int(str(i) + str(i)[-2::-1])
            if y >= N and is_prime(y): return y
