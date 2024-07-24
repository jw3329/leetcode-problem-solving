class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        min_size = [sys.maxsize] * 26
        min_size2 = sys.maxsize
        for i in range(len(points)):
            size = max(abs(points[i][0]), abs(points[i][1]))
            # check size with min_size
            j = ord(s[i]) - ord('a')
            if min_size[j] > size:
                min_size[j], size = size, min_size[j]
            # now we calculate min_size2
            min_size2 = min(min_size2, size)
        return sum(1 for count in min_size if count < min_size2)
