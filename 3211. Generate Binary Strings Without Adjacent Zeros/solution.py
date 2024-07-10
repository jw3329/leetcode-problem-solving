class Solution:
    def validStrings(self, n: int) -> List[str]:
        # from prev valid, operate with 0 and 1
        # 1
        # 01 10 11
        # from first 0, it should always be 1,
        # if 1, then choice of 0 or 1
        # make it into n
        
        def helper(curr, is_zero):
            if (curr, is_zero) in memo: return
            if len(curr) == n:
                res.add(curr)
                return
            if is_zero:
                helper(curr + '0', False)
            else:
                helper(curr + '1', False)
                helper(curr + '1', True)
            memo[(curr,is_zero)] = True
        
        res = set()
        memo = dict()
        helper('', True)
        helper('', False)
        return list(res)
