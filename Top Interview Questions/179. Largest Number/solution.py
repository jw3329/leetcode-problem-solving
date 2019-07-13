class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        class cmp(str):
            def __lt__(x,y):
                return x + y > y + x
        
        string = ''.join(sorted(map(str,nums), key=cmp))
        return string if string[0] != '0' else '0'
