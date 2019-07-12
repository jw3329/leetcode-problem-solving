class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:        
        res = 0
        for i in range(len(points)):
            map = {}
            max_val = overlap = 0
            for j in range(i+1,len(points)):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                
                if x == 0 and y == 0:
                    overlap += 1
                    continue
                
                gcd = self.gcd(x,y)
                if gcd != 0:
                    x /= gcd
                    y /= gcd
                
                if x in map:
                    if y in map[x]:
                        map[x][y] += 1
                    else:
                        map[x][y] = 1
                else:
                    map[x] = {y:1}
                max_val = max(max_val, map[x][y])
            res = max(res, max_val + 1 + overlap)
        return res
                
                
    def gcd(self,x,y):
        if y == 0: return x
        return self.gcd(y,x % y)
