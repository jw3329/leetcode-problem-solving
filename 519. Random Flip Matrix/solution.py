class Solution:

    def __init__(self, m: int, n: int):
        # if zero or one judge
        self.m = m
        self.n = n
        self.map = dict()
        self.reset()
        

    def flip(self) -> List[int]:
        self.total -= 1
        i = random.randint(0, self.total)
        x = self.map.get(i, i)
        # switch to total, very last index
        self.map[i] = self.map.get(self.total, self.total)
        self.map[self.total] = x
        return [x // self.n, x % self.n]

        

    def reset(self) -> None:
        self.total = self.m * self.n
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
