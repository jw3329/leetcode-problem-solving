class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        s_list = []
        self.dfs(s,0,s_list,res)
        return res
    
    
    def dfs(self,s,pos,s_list,res):
        if pos == len(s): res.append(s_list.copy())
        for i in range(pos,len(s)):
            if self.is_palindrome(s,pos,i):
                s_list.append(s[pos:i+1])
                self.dfs(s,i+1,s_list,res)
                s_list.pop()
        
        
    def is_palindrome(self,s, low, high):
        while low < high:
            if s[low] != s[high]: return False
            low += 1
            high -= 1
        return True
