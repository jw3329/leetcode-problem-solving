class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        # try to split
        # check if it has duplicate
        # get minimum
        
        # try one by one
        # left to right, check one by one
        # if unbalanced, then we keep searching
        
        def balanced(curr):
            if len(curr) <= 1: return True
            keys = list(curr.keys())
            # check if all values are same
            val = curr[keys[0]]
            for i in range(1, len(keys)):
                if curr[keys[i]] != val: return False
            return True
        
        def helper(index):
            if index == len(s): return 0
            if index in memo: return memo[index]
            res = sys.maxsize
            curr = dict()
            for i in range(index, len(s)):
                if s[i] not in curr:
                    curr[s[i]] = 0
                curr[s[i]] += 1
                if balanced(curr):
                    res = min(res, 1 + helper(i+1))
            memo[index] = res
            return res
        
        memo = dict()
        return helper(0)
