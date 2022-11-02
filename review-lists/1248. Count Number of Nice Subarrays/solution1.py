class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def at_most(k):
            res = 0
            i = 0
            n = len(nums)
            for j in range(n):
                k -= nums[j] % 2
                while k < 0:
                    k += nums[i] % 2
                    i += 1
                res += j - i + 1
            return res
        
        return at_most(k) - at_most(k-1)
