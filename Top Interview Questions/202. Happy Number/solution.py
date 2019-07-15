class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()
        while n != 1:
            if n in num_set: return False
            num_set.add(n)
            num = 0
            while n != 0:
                num += (n % 10) ** 2
                n = n // 10
            n = num
        return True
