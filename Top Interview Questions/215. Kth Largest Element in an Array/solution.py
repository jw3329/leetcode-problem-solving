class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.find_kth_smallest(nums, len(nums) - k + 1, 0, len(nums) - 1)
    
    def find_kth_smallest(self,nums,k,start,end):
        index = self.partition(nums,start,end)
        if index - start == k - 1: return nums[index]
        if index - start > k - 1:
            return self.find_kth_smallest(nums,k,start,index-1)
        return self.find_kth_smallest(nums,k - index + start - 1, index + 1, end)
    
    def partition(self,nums,start,end):
        pivot = nums[end]
        i = start - 1
        for j in range(start,end):
            if nums[j] <= pivot:
                i += 1
                self.swap(nums,i,j)
        self.swap(nums,i+1,end)
        return i+1
    
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
