class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n-2
        while k >= 0:
            if nums[k] < nums[k+1]:
                break
            k -= 1
        if k < 0:
            self.reverse(nums,0,n-1)
        else:
            l = n-1
            while l >= k:
                if nums[l] > nums[k]: break
                l -= 1
            # swapping
            self.swap(nums,k,l)
            
            #reverse
            self.reverse(nums,k+1,n-1)
            
    def reverse(self,nums,start,end):
        while start < end:
            self.swap(nums,start,end)
            start += 1
            end -= 1
        
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
