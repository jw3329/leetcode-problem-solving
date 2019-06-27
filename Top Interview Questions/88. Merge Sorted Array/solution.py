class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        new_list = [0 for _ in range(len(nums1))]
        
        num1_index = 0
        num2_index = 0
        new_index = 0
        while num1_index < m and num2_index < n:
            if nums1[num1_index] < nums2[num2_index]:
                new_list[new_index] = nums1[num1_index]
                num1_index += 1
            else:
                new_list[new_index] = nums2[num2_index]
                num2_index += 1
            new_index += 1
        
        while num1_index < m:
            new_list[new_index] = nums1[num1_index]
            num1_index += 1
            new_index += 1
            
        while num2_index < n:
            new_list[new_index] = nums2[num2_index]
            num2_index += 1
            new_index += 1
            
        # move into nums1
        
        for i in range(len(nums1)):
            nums1[i] = new_list[i]
            
