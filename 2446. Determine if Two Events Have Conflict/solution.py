class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        def is_bigger(a, b):
            h1, m1 = a.split(':')
            h2, m2 = b.split(':')
            return 60 * int(h1) + int(m1) >= 60 * int(h2) + int(m2)
        
        # a1 < b0 or b1 < a0 -> no conflict
        # a1 >= b0 and b1 >= a0
        
        return is_bigger(event1[1], event2[0]) and is_bigger(event2[1], event1[0])
