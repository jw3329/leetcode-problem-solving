class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        # bruteforce -> one student, tutor one by one, get maximum
        visited = [False] * len(mentors)
        
        def score(a, b):
            res = 0
            for i in range(len(a)):
                if a[i] == b[i]: res += 1
            return res
        
        def dfs(pos):
            if pos >= len(students): return 0
            res = 0
            for i in range(len(mentors)):
                if not visited[i]:
                    visited[i] = True
                    res = max(res, score(students[pos], mentors[i]) + dfs(pos+1))
                    visited[i] = False
            return res
                
        
        return dfs(0)
