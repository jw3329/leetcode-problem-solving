class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def partition(left, right):
            pivot = nums[right]
            i = left
            while i <= right:
                # check if i is less than pivot
                if nums[i] < pivot:
                    swap(i,left)
                    left += 1
                    i += 1
                elif nums[i] > pivot:
                    swap(i, right)
                    right -= 1
                else:
                    i += 1
            # now we return left and right
            return left, right
        
        def quickselect(k):
            left = 0
            right = len(nums)-1
            while left <= right:
                l,h = partition(left, right)
                if k > h:
                    left = h + 1
                elif k < l:
                    right = l - 1
                else:
                    return nums[l]
            return -1
                
        
        def shuffle():
            for i in range(len(nums)):
                index = random.randint(i,len(nums)-1)
                swap(i, index)
        
        shuffle()
        return quickselect(len(nums)-k)
