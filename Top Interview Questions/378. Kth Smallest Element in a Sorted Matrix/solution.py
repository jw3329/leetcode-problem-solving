class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            count = self.get_less_equal(matrix,mid)
            if count < k: lo = mid + 1
            else:
                hi = mid - 1
        return lo
    
    def get_less_equal(self,matrix,val):
        res = 0
        i, j = len(matrix) - 1, 0
        
        while i >= 0 and j < len(matrix):
            if matrix[i][j] > val: i -= 1
            else:
                res += i + 1
                j += 1
        return res
