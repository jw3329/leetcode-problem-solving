class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = collections.Counter(nums)
        # key -> count
        # make count -> keys
        freq = dict()
        for key, count in counter.items():
            if count not in freq:
                freq[count] = []
            freq[count].append(key)
        # now we have count -> keys
        res = []
        for i in range(n,-1,-1):
            if i in freq:
                while k > 0 and freq[i]:
                    k -= 1
                    res.append(freq[i].pop())
                if k == 0: break
        return res
