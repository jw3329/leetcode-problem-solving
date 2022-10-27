class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # within radius,
        # find point, where towers quality is maximum
        # each point, find points within radiuses, 
        # track maximum
        
        def get_reachable(x,y):
            # grab dict keys that is in between x-radius and x+radius
            res = []
            for tower_x in tower_map:
                if not x-radius <= tower_x <= x+radius: continue
                # check y next
                for tower_y in tower_map[tower_x]:
                    # check radius of distance
                    if distance(x,y,tower_x,tower_y) > radius: continue
                    res.append([tower_x, tower_y, tower_map[tower_x][tower_y]])
            return res
                
        
        def distance(x1,y1,x2,y2):
            return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
        
        def formula(x1, y1, x2, y2, q):
            return int(q / (1 + distance(x1,y1,x2,y2)))
        
        # set tower into map
        tower_map = dict()
        for tower in towers:
            if tower[0] not in tower_map:
                tower_map[tower[0]] = dict()
            if tower[1] not in tower_map[tower[0]]:
                tower_map[tower[0]][tower[1]] = 0
            tower_map[tower[0]][tower[1]] += tower[2]
        
        # iterate all coords
        quality = -1
        quality_x = -1
        quality_y = -1
        for x in range(51):
            for y in range(51):
                # find reachable coord
                reachables = get_reachable(x,y)
                curr_quality = 0
                for reachable in reachables:
                    curr_quality += formula(x,y,reachable[0], reachable[1], reachable[2])
                if curr_quality > quality:
                    quality = curr_quality
                    quality_x = x
                    quality_y = y
        return [quality_x, quality_y]
        
