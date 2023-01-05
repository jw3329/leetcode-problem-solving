class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # curr -> prev comb + curr one by one each
        
        def helper(n):
            if n == 0:
                return set([''])
            prev = helper(n-1)
            new_set = set()
            for comb in prev:
                c = tiles[n-1]
                for i in range(len(comb)+1):
                    new = comb[:i] + c + comb[i:]
                    new_set.add(new)
            return new_set | prev
                    
            
        
        return len(helper(len(tiles))) - 1
