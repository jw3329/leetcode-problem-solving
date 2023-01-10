class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # move origin
        x1 -= xCenter
        x2 -= xCenter
        y1 -= yCenter
        y2 -= yCenter
        min_x = min(x1*x1,x2*x2) if x1 * x2 > 0 else 0
        min_y = min(y1*y1,y2*y2) if y1 * y2 > 0 else 0
        return min_x + min_y <= radius * radius
