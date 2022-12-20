class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # remove num which is form of other reliable nums
        # track how many num has cut, 
        count = dict()
        for num in nums:
            count[num % space] = count.get(num % space, 0) + 1
        max_freq = max(count.values())
        res = sys.maxsize
        for num in nums:
            if count[num % space] == max_freq:
                res = min(res, num)
        return res
