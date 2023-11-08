class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.i = 0
        self.j = 0
        # i and j indicates, original place to insert into res
        self.vec2d = vec2d

    # @return {int} a next element
    def next(self):
        # possibly original place can be out, so make fix of it
        while self.j >= len(self.vec2d[self.i]):
            self.i += 1
            self.j = 0
        val = self.vec2d[self.i][self.j]
        self.j += 1
        return val
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # check possibilities
        ii = self.i
        jj = self.j
        
        while ii < len(self.vec2d) and jj >= len(self.vec2d[ii]):
            ii += 1
            jj = 0
        # if row is same, then we return false
        if ii == len(self.vec2d): return False
        return True

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
