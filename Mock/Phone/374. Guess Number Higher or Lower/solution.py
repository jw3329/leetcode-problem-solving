# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(1,n)
    
    def helper(self,start,end):
        mid_val = (start + end) // 2
        res = guess(mid_val)
        if res == 0: return mid_val
        if res == 1: return self.helper(mid_val+1,end)
        return self.helper(start,mid_val-1)
