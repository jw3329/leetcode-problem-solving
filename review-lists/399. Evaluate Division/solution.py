class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a = 2 * b
        # b = 3 * c
        # generate graph
        # for each query
        # find target, and weight of it, and return

        def calculate(query, visited):
            # so first one should be converted to second one
            source, target = query
            if source not in graph: return -1
            if source in visited: return -1
            visited.add(source)
            for adj in graph[source]:
                # check if there's available
                # if available, then just return
                # if not, then keep checking
                if target == adj:
                    return graph[source][adj]
                check = calculate([adj, target], visited)
                if check != -1: return graph[source][adj] * check
            visited.remove(source)
            return -1



        graph = dict()
        # a -> b -> value --> a = b * value
        # also should make, b = a / value

        for i, eq in enumerate(equations):
            if eq[0] not in graph:
                graph[eq[0]] = dict()
            graph[eq[0]][eq[1]] = values[i]
            if eq[1] not in graph:
                graph[eq[1]] = dict()
            graph[eq[1]][eq[0]] = 1 / values[i]
        res = []
        for query in queries:
            res.append(calculate(query, set()))
        return res
