class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def count_less(limit):
            res = 0
            i = 0
            j = len(nums) - 1
            while i < j:
                while i < j and nums[i] + nums[j] > limit:
                    j -= 1
                res += j - i
                i += 1
                
            return res
                
        
        nums.sort()
        return count_less(upper) - count_less(lower-1)
