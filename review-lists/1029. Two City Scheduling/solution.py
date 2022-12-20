class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        n = len(costs) // 2
        min_cost = 0
        for a,b in costs:
            refund.append(b-a)
            min_cost += a
        refund.sort()
        for i in range(n):
            min_cost += refund[i]
        return min_cost
