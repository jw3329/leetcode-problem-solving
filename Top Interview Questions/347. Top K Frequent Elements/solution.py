class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        collected = collections.Counter(nums)
        arr = sorted(collected, key=collected.get, reverse = True)
        return arr[:k]
