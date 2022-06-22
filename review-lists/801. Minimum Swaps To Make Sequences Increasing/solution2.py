class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        not_swap = 0
        swap = 1
        for i in range(1, N):
            not_swap2, swap2 = N, N
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                swap2 = swap + 1
                not_swap2 = not_swap
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                swap2 = min(swap2, not_swap + 1)
                not_swap2 = min(not_swap2, swap)
            swap, not_swap = swap2, not_swap2
        return min(swap, not_swap)
