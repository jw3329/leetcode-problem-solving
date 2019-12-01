class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance_map = {}
        
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            if distance not in distance_map:
                distance_map[distance] = []
            distance_map[distance].append(point)
        res = []
        sorted_key = sorted(distance_map.keys())
        i = 0
        while i < K:
            for key in sorted_key:
                for point in distance_map[key]:
                    res.append(point)
                    i += 1
                    if i == K: break
                if i == K: break
        return res

