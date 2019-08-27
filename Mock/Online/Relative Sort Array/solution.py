class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_counter = collections.Counter(arr1)
        res = []
        for num in arr2:
            while arr1_counter[num] > 0:
                res.append(num)
                arr1_counter[num] -= 1
            if not arr1_counter[num]: arr1_counter.pop(num)
        rest = []
        for key in sorted(arr1_counter.keys()):
            while arr1_counter[key] > 0:
                rest.append(key)
                arr1_counter[key] -= 1
        return res + rest
