class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counter = collections.Counter(nums)
        res = 0
        for key in counter:
            if target.find(key) != 0: continue
            if key + key == target:
                res += counter[key] * (counter[key] - 1)
            else:
                res += counter[key] * counter.get(target[len(key):], 0)
        return res
