class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        inserted_set = set()
        res = []
        
        for num in nums2:
            if num in nums1_set and num not in inserted_set: 
                res.append(num)
                inserted_set.add(num)
        return res

