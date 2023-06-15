class Bitset:

    def __init__(self, size: int):
        self.origin = [False] * size
        self.flipped = [True] * size
        self.size = size
        self.cnt = 0
        

    def fix(self, idx: int) -> None:
        if not self.origin[idx]:
            self.cnt += 1
        self.origin[idx] = True
        self.flipped[idx] = False

    def unfix(self, idx: int) -> None:
        if self.origin[idx]:
            self.cnt -= 1
        self.origin[idx] = False
        self.flipped[idx] = True

    def flip(self) -> None:
        self.cnt = self.size - self.cnt
        self.origin, self.flipped = self.flipped, self.origin

    def all(self) -> bool:
        return self.cnt == self.size

    def one(self) -> bool:
        return self.cnt >= 1
        

    def count(self) -> int:
        return self.cnt
        

    def toString(self) -> str:
        return ''.join(map(lambda x: str(int(x)), self.origin))
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
