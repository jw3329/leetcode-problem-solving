class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        record = {}
        while N > 0:
            cells_copy = [0] * len(cells)
            record[str(cells)] = N
            N -= 1
            for i in range(6):
                cells_copy[i+1] = 1 if cells[i] == cells[i+2] else 0
            cells = cells_copy
            if str(cells) in record:
                N %= record[str(cells)] - N
        return cells
