class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr.insert(0, 0)
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        res = 0
        count = collections.defaultdict(int)
        total = collections.defaultdict(int)
        for i in range(len(arr)):
            res += count[arr[i]] * (i - 1) - total[arr[i]]
            count[arr[i]] += 1
            total[arr[i]] += i
        return res
