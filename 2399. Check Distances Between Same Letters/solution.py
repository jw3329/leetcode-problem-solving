class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # map with index
        # if not true, then return false
        # return true
        
        index_map = dict()
        for i, c in enumerate(s):
            if c not in index_map:
                index_map[c] = i
            else:
                if not distance[ord(c) - ord('a')] == i - index_map[c] - 1:
                    return False
        return True
