class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # get maximum of middle coins
        # we sort, from last, get 2n index
        n = len(piles) // 3
        piles.sort()
        i = 0
        res = 0
        while i < n:
            res += piles[len(piles) - 2 * i - 2]
            i += 1
        return res
