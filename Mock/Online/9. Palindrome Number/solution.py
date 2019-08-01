class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        
        i,j = 0, len(str_x) - 1
        
        while i < j:
            if str_x[i] == str_x[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
