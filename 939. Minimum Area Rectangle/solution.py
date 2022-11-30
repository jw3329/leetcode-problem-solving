class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # key mapping x to y coord set
        # both points interation, once they find x,y coord same, they do calculation for mapping, then tracking min rec size
        # return
        
        coord_map = dict()
        res = sys.maxsize
        for point in points:
            if point[0] not in coord_map:
                coord_map[point[0]] = set()
            coord_map[point[0]].add(point[1])
        for p1 in points:
            for p2 in points:
                if p1[0] >= p2[0] or p1[1] >= p2[1]: continue
                # we just confirmed that neither matching
                if p2[1] in coord_map[p1[0]] and p1[1] in coord_map[p2[0]]:
                    res = min(res, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))
        return 0 if res == sys.maxsize else res
