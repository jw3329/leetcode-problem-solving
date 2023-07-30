class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def check(arr):
            j = 0
            for i in range(len(arr)):
                if arr[i] == p[j]:
                    j += 1
                if j == len(p): return True
            return False
        
        # binary search to find k
        left = 0
        right = len(removable)
        arr = list(s)
        while left < right:
            mid = left + (right - left + 1) // 2
            # mark / for removed one
            for i in range(mid):
                arr[removable[i]] = '/'
            # check now
            if check(arr):
                # we pass check, we try to grab more k
                left = mid
            else:
                arr = list(s)
                right = mid - 1
        return left
