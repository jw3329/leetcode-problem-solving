class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N
            
            if N >= 1:
                N -= 1
                cells = self.next_day(cells)
        return cells
            
        
    def next_day(self,cells):
        cells_copy = cells.copy()
        for i in range(1,len(cells) - 1):
            if cells[i-1] == cells[i+1]:
                cells_copy[i] = 1
            else:
                cells_copy[i] = 0
        cells_copy[0] = cells_copy[-1] = 0
        return cells_copy
