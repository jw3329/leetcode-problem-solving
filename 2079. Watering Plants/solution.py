class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # go back if you have no capacity
        pos = -1
        res = 0
        tank = capacity
        for i in range(len(plants)):
            # check if capacity is enough
            if tank >= plants[i]:
                # we increment number of steps first
                res += i - pos
                # reduce capacity
                tank -= plants[i]
                # update position
                pos = i
            else:
                # if not, we should reverse back
                # going back and coming will be, i + i + 1 -> 2*i + 1
                res += 2*i + 1
                # then update tank
                tank = capacity - plants[i]
                # then update pos
                pos = i
        return res
