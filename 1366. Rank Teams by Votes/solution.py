class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        l = len(votes[0])
        rank_map = dict()
        for vote in votes:
            for i in range(l):
                if vote[i] not in rank_map:
                    rank_map[vote[i]] = [0] * l
                rank_map[vote[i]][i] += 1
        c_list = list(votes[0])
        def cmp(x,y):
            for i in range(l):
                if rank_map[x][i] != rank_map[y][i]:
                    return rank_map[y][i] - rank_map[x][i]
            return ord(x) - ord(y)
        
        # sort it by order
        c_list.sort(key=cmp_to_key(cmp))
        return ''.join(c_list)
        