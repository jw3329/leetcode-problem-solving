class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # id -> set()
        # iterate
        id_set = dict()
        for log in logs:
            if log[0] not in id_set:
                id_set[log[0]] = set()
            id_set[log[0]].add(log[1])
        res = [0] * k
        for _set in id_set.values():
            res[len(_set) - 1] += 1
        return res
