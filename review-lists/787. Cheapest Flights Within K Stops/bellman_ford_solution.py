class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [sys.maxsize] * n
        cost[src] = 0
        for i in range(k+1):
            temp = cost.copy()
            for f in flights:
                curr, next, price = f
                if cost[curr] == sys.maxsize: continue
                temp[next] = min(temp[next], cost[curr] + price)
            cost = temp
        return -1 if cost[dst] == sys.maxsize else cost[dst]
        
