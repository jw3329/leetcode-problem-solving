class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        res = mat[0]
        for i in range(1, m):
            res = self.kth_smallest_pairs(res, mat[i])
        return res[k-1]
    
    def kth_smallest_pairs(self, nums1, nums2):
        i = 0
        k = 200
        heap = []
        res = []
        while i < len(nums1) and i < k:
            heapq.heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
            i += 1
        while k > 0 and heap:
            curr = heapq.heappop(heap)
            res.append(curr[0])
            if curr[3] == len(nums2) - 1: continue
            heapq.heappush(heap, (curr[1] + nums2[curr[3] + 1], curr[1], nums2[curr[3] + 1], curr[3] + 1))
            k -= 1
        return res
