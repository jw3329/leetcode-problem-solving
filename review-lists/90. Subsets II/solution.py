class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # counter into map
        # {1 : 1, 2: 2}
        # if no key, return []
        # [2], [2, 2], []
        # get all possible of rest
        # get current possible, [1], []
        counter = collections.Counter(nums)
        keys = counter.keys()
        def helper():
            if len(counter) == 0:
                return [[]]
            keys = list(counter.keys())
            num = counter[keys[0]]
            counter.pop(keys[0])
            rest = helper()
            res = []
            for i in range(num+1):
                comb = [keys[0]] * i
                for r in rest:
                    res.append(comb + r)
            return res
                
        
        return helper()
        
