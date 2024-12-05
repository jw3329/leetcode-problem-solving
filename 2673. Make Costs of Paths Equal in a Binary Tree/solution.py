class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # left sum should be equal
        # right sum should be equal
        # to the bottom
        
        # find sum of child to bottom
        # left sum, right sum
        # right -> 10
        # left -> 7
        # compare, increment left by 3
        
        def helper(i):
            if i >= n: return 0
            left_max = helper(2*i+1)
            right_max = helper(2*i+2)
            # assume we have max
            self.res += abs(left_max - right_max)
            return cost[i] + max(left_max, right_max)
        
        self.res = 0
        helper(0)
        return self.res
        
