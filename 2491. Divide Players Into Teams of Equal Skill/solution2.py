class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        counter = collections.Counter(skill)
        s = 2 * sum(skill) // len(skill)
        res = 0
        for k, v in counter.items():
            if v != counter[s-k]: return -1
            res += k * v * (s-k)
        return res // 2
