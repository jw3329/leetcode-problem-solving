class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        x = y = 0
        i = 0
        for inst in instructions:
            if inst == 'L':
                i = (i + 3) % 4
            elif inst == 'R':
                i = (i + 1) % 4
            else:
                x += dirs[i][0]
                y += dirs[i][1]
        return x == 0 and y == 0 or i > 0
