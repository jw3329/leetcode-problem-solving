class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        val = [1] * len(primes)
        index = [0] * len(primes)
        ugly = [0] * n
        next = 1
        for i in range(n):
            ugly[i] = next
            next = sys.maxsize
            
            for j in range(len(primes)):
                if ugly[i] == val[j]:
                    val[j] = ugly[index[j]] * primes[j]
                    index[j] += 1
                next = min(next, val[j])
        return ugly[-1]
