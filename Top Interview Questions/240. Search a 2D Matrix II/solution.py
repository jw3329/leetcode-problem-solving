class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        i = 0
        j = len(matrix[0]) - 1
        
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target: return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
