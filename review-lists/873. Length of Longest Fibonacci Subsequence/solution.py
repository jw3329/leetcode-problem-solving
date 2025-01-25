class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        res = 2
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                a, b, l = arr[i], arr[j], 2
                while a + b in s:
                    a, b, l = b, a+b, l+1
                res = max(res, l)
        return res if res > 2 else 0
