class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2: return
        index = n-1
        while index > 0:
            if nums[index - 1 ] < nums[index]:
                break
            index -= 1
        if index == 0:
            self.reverseSort(nums,0,n-1)
            return
        val = nums[index - 1]
        j = n-1
        while j >= index:
            if nums[j] > val:
                break
            j -= 1
        self.swap(nums,j,index-1)
        # nums[j],nums[index-1] = nums[index-1],nums[j]
        self.reverseSort(nums,index,n-1)
        
        
    def reverseSort(self,nums,start,end):
        if start > end: return
        for i in range(start,(end+start) // 2 + 1):
            self.swap(nums,i,start+end-i)
            # nums[i],nums[start+end-i] = nums[start+end-i],nums[i]
            
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
