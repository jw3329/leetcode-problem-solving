class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # large to small
        # later for smaller, it's better to put into index
        # 70 71 61 50 52 44
        # 50 70 52 61 44 71
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for person in people:
            res.insert(person[1], person)
        return res
