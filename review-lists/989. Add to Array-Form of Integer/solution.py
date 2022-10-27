class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(num)-1,-1,-1):
            res.insert(0, (num[i] + k) % 10)
            k = (num[i] + k) // 10
        while k > 0:
            res.insert(0, k % 10)
            k //= 10
        return res
