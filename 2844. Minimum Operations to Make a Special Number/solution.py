class Solution:
    def minimumOperations(self, num: str) -> int:
        zero_found = False
        five_found = False
        
        for i in range(len(num) - 1, -1, -1):
            
            if zero_found:
                if num[i] == '0' or num[i] == '5': return len(num) - 2 - i
            if five_found:
                if num[i] == '2' or num[i] == '7': return len(num) - 2 - i
            
            if num[i] == '5': five_found = True
            if num[i] == '0': zero_found = True
        if zero_found: return len(num) - 1
        return len(num)
