class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create email map
        email_map = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_map[email].append(i)
        res = []
        visited = [False] * len(accounts)
        
        def dfs(i, email_set):
            # if visited, then return
            if visited[i]: return
            visited[i] = True
            # iterate account i emails, and collect it into email set, dfs into it
            for email in accounts[i][1:]:
                email_set.add(email)
                # link to associated index
                for j in email_map[email]:
                    dfs(j, email_set)
        
        # try to iterate each accounts, which was not visited,
        # and grab all emails associated with it
        for i, account in enumerate(accounts):
            # skip if visited
            if visited[i]: continue
            email_set = set()
            # make dfs to put all emails into email set
            dfs(i, email_set)
            # now we have email set, put into res
            res.append([account[0]] + sorted(email_set))
        return res
