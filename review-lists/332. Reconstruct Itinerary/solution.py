class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create graph, make it into sorted for each node
        # go and pop, then store into res
        graph = collections.defaultdict(list)
        self.num_ticket = len(tickets)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        for key in graph:
            graph[key].sort()
        res = []
        
        def dfs(curr):
            for i in range(len(graph[curr])):
                dest = graph[curr].pop(i)
                res.append(dest)
                self.num_ticket -= 1
                dfs(dest)
                if self.num_ticket == 0:
                    return
                self.num_ticket += 1
                res.pop()
                graph[curr].insert(i, dest)
        res.append('JFK')
        dfs('JFK')
        return res
