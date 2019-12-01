class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = collections.Counter(ages)
        return sum(self.request_condition(a,b) * c[a] * (c[b] - (a == b)) for a in c for b in c)
    
    def request_condition(self,A,B):
        return not (B <= 0.5 * A + 7 or B > A or (B > 100 and A < 100))
