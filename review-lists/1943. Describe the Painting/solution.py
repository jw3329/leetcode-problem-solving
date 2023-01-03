class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        paint_map = collections.defaultdict(int)
        for s,e,c in segments:
            paint_map[s] += c
            paint_map[e] -= c
        prev = None
        color = 0
        res = []
        for curr in sorted(paint_map):
            # if color, this means painted, if 0, not painted
            if color:
                res.append([prev, curr, color])
            color += paint_map[curr]
            prev = curr
        return res
