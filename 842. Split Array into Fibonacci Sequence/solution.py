class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        # first, second
        # check if third is there,
        # then last two, then fourth -> first and second is determining whole
        
        def dfs(i, res):
            if i == len(num): return True
            # check first two
            # last two addition
            fib = res[-1] + res[-2]
            fib_str = str(fib)
            if not is_digit(fib_str): return False
            if num[i:i+len(fib_str)] == fib_str:
                res.append(fib)
                return dfs(i+len(fib_str), res)
            return False
        
        def is_digit(digit):
            if digit == '0': return True
            if digit[0] == '0': return False
            return int(digit) < 0x80000000
            
        
        for i in range(1, len(num)):
            digit1 = num[:i]
            if not is_digit(digit1): continue
            for j in range(i+1,len(num)):
                # choose first two
                digit2 = num[i:j]
                if not is_digit(digit2): continue
                # now dfs using current digits
                res = [int(digit1), int(digit2)]
                if dfs(len(digit1) + len(digit2), res): return res
        return []
