class ThroneInheritance:

    def __init__(self, kingName: str):
        self.map = collections.defaultdict(list)
        self.root = kingName
        self.deathset = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.map[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.deathset.add(name)

    def getInheritanceOrder(self) -> List[str]:
        # starting from root
        # dfs into each child
        # after getting result, remove lists from deathset
        res = self.dfs(self.root)
        # remove dead list
        return list(filter(lambda name : name not in self.deathset, res))
        
        
    def dfs(self, root):
        if len(self.map[root]) == 0:
            return [root]
        res = [root]
        for child in self.map[root]:
            res += self.dfs(child)
        return res
        
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
