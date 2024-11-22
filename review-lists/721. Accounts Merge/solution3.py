accounts = dict(
    C1=["johnsmith@mail.com", "john_newyork@mail.com"],
    C2=["johnsmith@mail.com", "john00@mail.com"],
    C3=["mary@mail.com"],
    C4=[
        "johnnybravo@mail.com",
    ],
)


def build_email_group_graph():
    res = dict()
    for group in accounts:
        for email in accounts[group]:
            if email not in res:
                res[email] = []
            res[email].append(group)
    return res


def solve():

    def dfs(email):
        if email not in email_group_graph:
            return set()
        if email in visited:
            return set()
        visited.add(email)
        res = set()
        for group in email_group_graph[email]:
            res.add(group)
            for e in accounts[group]:
                res |= dfs(e)
        return res

    # do also with it
    email_group_graph = build_email_group_graph()
    # form up graph
    # johnsmith@mail.com -> [C1, C2]
    # get final of it
    res = dict()
    visited = set()
    for email in email_group_graph:
        # do email for dfs
        if email in visited:
            continue
        res[email] = dfs(email)
    return res.values()


print(solve())


def solve2():

    def find(key):
        if key == parents[key]:
            return key
        parents[key] = find(parents[key])
        return parents[key]

    # do union find way
    # make union find for email related
    # create graph first
    email_group_graph = build_email_group_graph()
    parents = dict()
    # find all root, then relate that all to the group, then return
    for email in email_group_graph:
        parents[email] = email
    # now do union
    for account in accounts:
        root_email = accounts[account][0]
        for sub_email in accounts[account][1:]:
            parents[sub_email] = find(root_email)
    res = dict()
    for email in email_group_graph:
        root_email = find(email)
        # now we relate
        if root_email not in res:
            res[root_email] = set()
        res[root_email] |= set(email_group_graph[email])
    return res.values()


print(solve2())
