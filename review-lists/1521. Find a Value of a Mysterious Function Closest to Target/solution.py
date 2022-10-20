class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        # find value of sub array
        # with the value of & operations
        # which makes closest to target
        
        # and operator decreases for multiple
        # we define set array, going from top to bottom,
        # make operation for set for each,
        # after we gather all from set at 0 index, we get minimum diff of target, then return
        n = len(arr)
        sets = [set() for _ in range(n)]
        sets[n-1].add(arr[n-1])
        for i in range(n-2, -1, -1):
            # we should first add itself value
            sets[i].add(arr[i])
            # now for all next sets index, do and operation, then insert
            for value in sets[i+1]:
                sets[i].add(arr[i] & value)
        
        # now find differences
        min_val = sys.maxsize
        for i in range(n):
            for value in sets[i]:
                min_val = min(min_val, abs(value - target))
        return min_val
