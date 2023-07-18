class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # iterate first box
        # then s1 - item1
        # we need something s1 - item1 = s2 - item2
        # if s2 > s1, s2 - s1 = item2 - item1
        # item2 = item1 + s2 - s1
        s1 = sum(aliceSizes)
        s2 = sum(bobSizes)
        delta = (s2 - s1) // 2
        b_set = set(bobSizes)
        for c in aliceSizes:
            if c + delta in b_set: return [c, c + delta]
        return []
