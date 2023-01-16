class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # curr -> prev + 1 + inverted
        # calculate inverted
        
        def s(i):
            if i == 1: return '0'
            prev = s(i-1)
            res = ''
            for i in range(len(prev)-1,-1,-1):
                c = '0' if prev[i] == '1' else '1'
                res += c
            return prev + '1' + res
        
        
        return  s(n)[k-1]
