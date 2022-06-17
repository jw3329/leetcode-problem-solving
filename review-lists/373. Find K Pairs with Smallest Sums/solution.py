class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        while k > 0 and heap:
            k -= 1
            _, num1, num2, num2_index = heapq.heappop(heap)
            res.append([num1, num2])
            if num2_index + 1 == len(nums2): continue
            heapq.heappush(heap, (num1 + nums2[num2_index+1], num1, nums2[num2_index+1], num2_index + 1))
        return res
