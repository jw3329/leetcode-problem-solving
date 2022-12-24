class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # iterate, check if order same, add up to pair
        # each row and col has identical, so we can store
        # store in set of col, with frequency of map
        # key -> concate num, with freq val
        # each row, iterate, find key, add up to sum
        freq = dict()
        for j in range(len(grid[0])):
            temp = []
            for i in range(len(grid)):
                temp.append(str(grid[i][j]))
            key = ','.join(temp)
            if key not in freq:
                freq[key] = 0
            freq[key] += 1
        res = 0
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(str(grid[i][j]))
            key = ','.join(temp)
            if key in freq:
                res += freq[key]
        return res
