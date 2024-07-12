class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # count the key
        # all divide by 24
        # iterate with two pointer
        for i in range(len(hours)):
            hours[i] = hours[i] % 24
        hours_counter = collections.Counter(hours)
        # 0 ~ 23
        res = 0
        for i in range(13):
            # check if same
            other = (24 - i) % 24
            if other not in hours_counter: continue
            if i == other:
                res += hours_counter[i] * (hours_counter[i] - 1) // 2
            else:
                res += hours_counter[i] * hours_counter[other]
        return res
