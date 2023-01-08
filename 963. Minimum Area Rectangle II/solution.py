class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # diagonal, mid point, and same line -> box creation possible
        
        def dist(i,j):
            return (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) * (points[i][1] - points[j][1])
        
        n = len(points)
        point_map = dict()
        for i in range(n):
            for j in range(i+1, n):
                d = dist(i,j)
                mid_x = points[i][0] + points[j][0]
                mid_y = points[i][1] + points[j][1]
                key = (d,mid_x,mid_y)
                if key not in point_map:
                    point_map[key] = []
                point_map[key].append((i,j))
        min_val = sys.maxsize
        for key in point_map:
            l = point_map[key]
            if len(l) == 1: continue
            for i in range(len(l)):
                p1_index = l[i][0]
                for j in range(i+1, len(l)):
                    p2_index = l[j][0]
                    p3_index = l[j][1]
                    min_val = min(min_val, math.sqrt(dist(p1_index, p2_index) * dist(p1_index, p3_index)))
        return min_val if min_val != sys.maxsize else 0
                
