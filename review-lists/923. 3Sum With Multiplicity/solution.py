class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # do freq count of map
        # take keys and sort
        # if things make 0, then add each multiple to res
        counter = collections.Counter(arr)
        res = 0
        for i in counter:
            for j in counter:
                k = target - i - j
                if k not in counter: continue
                if i == j == k:
                    res += counter[i] * (counter[i]-1) * (counter[i]-2) // 6
                elif i == j != k:
                    res += counter[i] * (counter[i]-1) * (counter[k]) // 2
                elif i < j < k:
                    res += counter[i] * counter[j] * counter[k]
        return res % (10**9 + 7)
