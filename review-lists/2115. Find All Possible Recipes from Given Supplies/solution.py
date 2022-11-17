class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # each ingredient pointing to recipe,
        # from no pointings, put into queue,
        # if no more degree made on food, add to queue
        # if food in recipes, add to res then return
        
        # so when queue iterates, curr will remove all related degrees, when degree is 0, then put that into queue also
        # if 0 is in recipes, then append that into res
        res = []
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for recipe, ingredient in zip(recipes, ingredients):
            for sub in ingredient:
                graph[sub].append(recipe)
                degree[recipe] += 1
        queue = deque(supplies)
        while queue:
            curr = queue.popleft()
            for adj in graph[curr]:
                degree[adj] -= 1
                if degree[adj] == 0:
                    res.append(adj)
                    queue.append(adj)
        return res
