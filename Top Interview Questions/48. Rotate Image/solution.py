class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.rotateHelper(matrix, 0, len(matrix) - 1)

    def rotateHelper(self, matrix, start, end):
        if start >= end:
            return
        self.rotateHelper(matrix, start+1, end-1)
        # start == 1, end == 2
        for i in range(end - start):
            temp = matrix[start][start + i]
            matrix[start][start + i] = matrix[end-i][start]
            matrix[end-i][start] = matrix[end][end-i]
            matrix[end][end-i] = matrix[start + i][end]
            matrix[start + i][end] = temp


s = Solution()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

matrix3 = [[4, 8], [3, 6]]

s.rotate(matrix)
s.rotate(matrix2)
s.rotate(matrix3)


print(matrix)
print(matrix2)
print(matrix3)
