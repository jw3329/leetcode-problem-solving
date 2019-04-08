class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.getFirst(nums,0,len(nums)-1,target),self.getSecond(nums,0,len(nums)-1,target)]
    
    def getFirst(self,nums,low,high,target):
        if low > high: return -1
        mid = (high - low) // 2 + low
        if nums[mid] == target:
            if mid - 1 < 0 or nums[mid - 1] != target:
                return mid
            return self.getFirst(nums,low,mid-1,target)
        if nums[mid] < target:
            return self.getFirst(nums,mid+1,high,target)
        return self.getFirst(nums,low,mid-1,target)
    
    def getSecond(self,nums,low,high,target):
        if low > high: return -1
        mid = (high - low) // 2 + low
        if nums[mid] == target:
            if mid + 1 >= len(nums) or nums[mid+1] != target:
                return mid
            return self.getSecond(nums,mid+1,high,target)
        if nums[mid] < target:
            return self.getSecond(nums,mid+1,high,target)
        return self.getSecond(nums,low,mid-1,target)
