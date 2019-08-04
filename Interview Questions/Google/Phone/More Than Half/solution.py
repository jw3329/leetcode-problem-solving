class Solution:
    
    def __init__(self,log):
        self.log = log

    def is_more_than_half(self,start,end,log_type):
        map = {}
        for i in range(start,end+1):
            if self.log[i] not in map:
                map[self.log[i]] = 0
            map[self.log[i]] += 1
        
        half = (end - start + 1) // 2

        if map[log_type] and map[log_type] > half: return True
        return False


s = Solution([6,6,6,7,3,8])

print(s.is_more_than_half(0,3,6))
print(s.is_more_than_half(1,4,6))
print(s.is_more_than_half(2,5,7))
