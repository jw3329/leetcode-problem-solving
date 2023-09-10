class Solution:
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0
        used = set()
        for c, freq in counter.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res
