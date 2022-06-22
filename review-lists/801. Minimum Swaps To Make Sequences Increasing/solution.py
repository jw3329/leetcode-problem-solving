class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        not_swap, swap = [N] * N, [N] * N
        not_swap[0] = 0
        swap[0] = 1
        for i in range(1, N):
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                swap[i] = swap[i-1] + 1
                not_swap[i] = not_swap[i-1]
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                swap[i] = min(swap[i], not_swap[i-1] + 1)
                not_swap[i] = min(not_swap[i], swap[i-1])
        return min(swap[N-1], not_swap[N-1])
