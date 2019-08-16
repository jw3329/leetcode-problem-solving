class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pairs = {}
        value_pairs = {}
        
        for i in range(len(equations)):
            equation = equations[i]
            if equation[0] not in pairs:
                pairs[equation[0]] = []
                value_pairs[equation[0]] = []
            if equation[1] not in pairs:
                pairs[equation[1]] = []
                value_pairs[equation[1]] = []
            pairs[equation[0]].append(equation[1])
            pairs[equation[1]].append(equation[0])
            value_pairs[equation[0]].append(values[i])
            value_pairs[equation[1]].append(1/values[i])
            
        res = []
        
        for query in queries:
            value = self.dfs(query[0],query[1],pairs,value_pairs,set(),1)
            res.append(value if value else -1)
        return res
    
    def dfs(self,start,end,pairs,value_pairs,visited,value):
        if start in visited: return 0
        if start not in pairs: return 0
        if start == end: return value
        visited.add(start)
        
        str_list = pairs[start]
        value_list = value_pairs[start]
        
        for i in range(len(str_list)):
            res = self.dfs(str_list[i],end,pairs,value_pairs,visited,value * value_list[i])
            if res: return res
        return 0
