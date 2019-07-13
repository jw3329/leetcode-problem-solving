class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0: return '0'
        res = '-' if (numerator > 0) ^ (denominator > 0) else ''
        num = abs(numerator)
        den = abs(denominator)
        
        res += str(num // den)
        num %= den
        
        if num == 0:
            return res
        
        res += '.'
        map = {}
        
        while num != 0:
            num *= 10
            res += str(num // den)
            num %= den
            
            if num in map:
                index = map[num]
                res = res[:index] + '(' + res[index:] + ')'
                break
            else:
                map[num] = len(res)
        return res
