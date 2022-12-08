class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # set curr sum of index
        # track curr sum % k
        # if found curr sum in map -> there's at least one solution
        # else put it into map
        curr = 0
        index_map = dict()
        index_map[0] = -1
        for i, num in enumerate(nums):
            curr = (curr + num) % k
            if curr in index_map:
                # check if curr i is >= 2
                if i - index_map[curr] >= 2: return True
            else:
                index_map[curr] = i
        return False
