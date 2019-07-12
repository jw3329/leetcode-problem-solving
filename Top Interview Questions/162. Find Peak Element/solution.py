class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = [-sys.maxsize] + nums + [-sys.maxsize]
        return self.helper(new_nums,0,len(new_nums) - 1) - 1
    
    def helper(self,nums,start,end):
        if end - start < 2: return -1
        mid = (start + end) // 2
        if nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        
        val = self.helper(nums,mid,end)
        return val if val != -1 else self.helper(nums,start,mid)
