class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [0 for _ in range(len(nums))]
        size = 0
        
        for num in nums:
            i,j = 0, size
            
            while i != j:
                m = (i + j) // 2
                if tail[m] < num:
                    i = m + 1
                else:
                    j = m
            tail[i] = num
            if i == size: size += 1
        return size
