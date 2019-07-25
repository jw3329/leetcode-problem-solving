class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        
        for num in nums1:
            if num not in map:
                map[num] = 0
            map[num] += 1
        res = []
        for num in nums2:
            if num in map and map[num] > 0:
                res.append(num)
                map[num] -= 1
        return res
