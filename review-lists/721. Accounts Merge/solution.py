class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        owner = dict()
        parents = dict()
        union = dict()
        
        def find(i):
            if i != parents[i]:
                parents[i] = find(parents[i])
            return parents[i]
        
        for account in accounts:
            for email in account[1:]:
                parents[email] = email
                owner[email] = account[0]
        # now, union for each email set
        for account in accounts:
            p = find(account[1])
            for email in account[2:]:
                parents[find(email)] = p
        # union each email
        for account in accounts:
            p = find(account[1])
            if p not in union:
                union[p] = set()
            for email in account[1:]:
                union[p].add(email)
        res = []
        for p in union:
            res.append([owner[p]] + sorted(union[p]))
        return res
