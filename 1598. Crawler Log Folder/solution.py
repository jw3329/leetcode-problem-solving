class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            test = log[:-1]
            if test == '.':
                continue
            if test == '..':
                if res > 0:
                    res -= 1
            else:
                res += 1
        return res
                
