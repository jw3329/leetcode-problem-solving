class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        p = [i for i in range(n)]
        primes = collections.defaultdict(list)
        
        def prime_set(num):
            # if num is prime, and if it's divisible, divide, and union prime set of divided
            for i in range(2, int(num ** (1/2)) + 1):
                if num % i == 0:
                    return prime_set(num // i) | set([i])
            return set([num])
        
        def find(num):
            if p[num] == num: return p[num]
            p[num] = find(p[num])
            return p[num]
        
        def union(num1, num2):
            p_num1 = find(num1)
            p_num2 = find(num2)
            p[p_num2] = p_num1
        
        for i, num in enumerate(nums):
            pr_set = prime_set(num)
            for pr in pr_set: primes[pr].append(i) # nums[i] is divisible by key
        for value in primes.values():
            for i in range(1, len(value)):
                union(value[i], value[i-1])
        return max(collections.Counter([find(i) for i in range(n)]).values())
            
