class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        pascal_triangle = self.generate(numRows-1)
        last_row = [1]
        last_before = pascal_triangle[-1]
        for i in range(len(last_before)-1):
            last_row.append(last_before[i] + last_before[i+1])
        last_row.append(1)
        pascal_triangle.append(last_row)
        return pascal_triangle
