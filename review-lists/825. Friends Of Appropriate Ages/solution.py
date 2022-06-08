class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = collections.Counter(ages)
        res = 0
        for x in counter:
            for y in counter:
                if self.condition(x, y):
                    if x == y:
                        res += counter[x] * (counter[x] - 1)
                    else:
                        res += counter[x] * counter[y]
        return res
    
    def condition(self, x, y):
        return not (y <= 0.5 * x + 7 or y > x)
