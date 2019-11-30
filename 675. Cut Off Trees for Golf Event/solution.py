class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        val = 0
        curr_x = 0
        curr_y = 0
        heap = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1: 
                    heapq.heappush(heap,(forest[i][j], i, j))
        while heap:
            index = heapq.heappop(heap)[1:]
            distance = self.bfs(forest,curr_x,curr_y,index[0],index[1])
            if distance == sys.maxsize: return -1
            val += distance
            forest[index[0]][index[1]] = 1
            curr_x = index[0]
            curr_y = index[1]
        return val
    
    def bfs(self,forest,curr_x,curr_y,dest_x,dest_y):
        visited = [[False for _ in range(len(forest[0]))] for _ in range(len(forest))]
        
        queue = [(curr_x,curr_y)]
        dir_x = [1,0,-1,0]
        dir_y = [0,1,0,-1]
        step = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr[0] == dest_x and curr[1] == dest_y: return step
                if visited[curr[0]][curr[1]]: continue
                visited[curr[0]][curr[1]] = True
                for k in range(4):
                    x = curr[0] + dir_x[k]
                    y = curr[1] + dir_y[k]
                    if x >= 0 and x < len(forest) and y >= 0 and y < len(forest[0]) and forest[x][y] != 0:
                        queue.append((x,y))
            step += 1
        return sys.maxsize
