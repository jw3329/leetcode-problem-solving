class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s,wordDict,{})
    
    def dfs(self,s,wordDict,map):
        if s in map: return map[s]
        res = []
        if not s:
            res.append('')
            return res
        for word in wordDict:
            if len(s) >= len(word) and s[:len(word)] == word:
                sub_list = self.dfs(s[len(word):], wordDict,map)
                for sub in sub_list:
                    res.append(word + (' ' if sub else '') + sub)
        map[s] = res
        return res
