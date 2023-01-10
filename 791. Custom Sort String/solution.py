class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # count, then sort
        counter = collections.Counter(s)
        res = ''
        for c in order:
            while counter[c] > 0:
                counter[c] -= 1
                res += c
        for c in s:
            while counter[c] > 0:
                counter[c] -= 1
                res += c
        return res
