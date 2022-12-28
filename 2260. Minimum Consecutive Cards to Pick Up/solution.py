class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # track last index and track min length of it
        index_map = dict()
        min_length = sys.maxsize
        for i in range(len(cards)):
            if cards[i] not in index_map:
                index_map[cards[i]] = i
            else:
                # compare min length with last
                min_length = min(min_length, i - index_map[cards[i]] + 1)
                index_map[cards[i]] = i
        return -1 if min_length == sys.maxsize else min_length
