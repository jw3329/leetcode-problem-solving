class Solution:
    
    def solve(self,matrix):
        queue = [matrix]
        goal = [[1,2,3,4],[5,6,7,8]]
        times = 0
        visited = set()
        while queue:
            curr = queue.pop(0)
            if str(curr) in visited: continue
            visited.add(str(curr))
            if curr == goal:
                return times
            queue.append(self.rotate(curr))
            queue.append(self.swap(curr))
            queue.append(self.shift(curr))
            times += 1
        return -1


    def rotate(self,matrix):
        new_matrix = [row[:] for row in matrix]
        temp = new_matrix[0][1]
        new_matrix[0][1] = new_matrix[1][1]
        new_matrix[1][1] = new_matrix[1][2]
        new_matrix[1][2] = new_matrix[0][2]
        new_matrix[0][2] = temp
        return new_matrix

    def swap(self,matrix):
        new_matrix = [row[:] for row in matrix]
        for i in range(4):
            new_matrix[0][i], new_matrix[1][i] = new_matrix[1][i],new_matrix[0][i]
        return new_matrix



    def shift(self,matrix):
        new_matrix = [row[:] for row in matrix]
        for j in range(2):
            temp = new_matrix[j][3]
            for i in range(2,-1,-1):
                new_matrix[j][i+1] = new_matrix[j][i]
            new_matrix[j][0] = temp
        return new_matrix


s = Solution()

matrix = [[4,2,6,5],[1,8,7,3]]
print(s.solve(matrix))
