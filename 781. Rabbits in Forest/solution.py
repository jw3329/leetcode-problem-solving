class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # if 1 in pair, then that's one color
        # 1 1
        # 2 2 2
        # 3 3 3 3 -> one color
        # color i should appear i + 1 times, otherwise, each will increment i + 1
        # if we have 13 10s, then 11 * 2
        # if we have 11 10s, 
        # add key + 1 times ceil of division
        counter = collections.Counter(answers)
        res = 0
        for key in counter:
            res += (key + 1) * math.ceil(counter[key] / (key + 1))
        return res
