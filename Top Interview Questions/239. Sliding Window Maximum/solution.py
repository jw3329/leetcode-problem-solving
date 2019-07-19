class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        n = len(nums)
        res = [0 for _ in range(n - k + 1)]
        
        ri = 0
        
        q = []
        for i in range(n):
            while q and q[0] < i - k + 1:
                q.pop(0)
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res[ri] = nums[q[0]]
                ri += 1
        return res
