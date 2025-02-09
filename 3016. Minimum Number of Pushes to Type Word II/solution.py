class Solution:
    def minimumPushes(self, word: str) -> int:
        # 2 ~ 9 valid -> total 8
        # no sort required
        # sort by freq count
        # map from top to bottom
        # after 8, next map
        counter = collections.Counter(word)
        # now sort by freq count
        items = sorted(counter.items(), key=lambda x: -x[1])
        res = 0
        # iterate, after count of 8, then add multiple
        multiple = 1
        total = 0
        for c, count in items:
            res += multiple * count
            # increment total
            total += 1
            if total == 8:
                total = 0
                multiple += 1
        return res
