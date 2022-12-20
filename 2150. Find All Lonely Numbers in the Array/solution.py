class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        res = []
        for key in counter:
            if counter[key] == 1:
                if key - 1 not in counter and key + 1 not in counter:
                    res.append(key)
        return res
