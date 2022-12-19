class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        # x -> get random number
        # get random number from 0 to 360
        # r cos t -> x --> cos t -> x / r     root( r^2 - x^2 )
        # r sin t -> y
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        

    def randPoint(self) -> List[float]:
        theta = random.uniform(0, 2*math.pi)
        R = self.radius * math.sqrt(random.uniform(0, 1))
        return [self.x_center + R * math.cos(theta), self.y_center + R * math.sin(theta)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
