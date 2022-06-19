class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # counter
        # key sorted
        box_counter = collections.defaultdict(int)
        for box_type in boxTypes:
            box_counter[box_type[1]] += box_type[0]
        res = 0
        for key in sorted(box_counter.keys(), reverse=True):
            # if value is larger than truck size, return with trucksize multiplied
            # if value is less equal, then subtract truckSize by value amount
            val = box_counter[key]
            if val >= truckSize:
                res += key * truckSize
                return res
            res += val * key
            truckSize -= val
        return res
