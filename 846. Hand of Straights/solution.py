class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # map count
        # iterate each, check at least 1 for consecutives
        # if not fulfilled, then false
        counter = collections.Counter(hand)
        count = len(hand)
        # iterate from sorted
        keys = sorted(counter.keys())
        for i in range(len(keys)):
            # removal of count
            init_count = counter[keys[i]]
            if init_count == 0: continue
            counter[keys[i]] -= init_count
            count -= init_count
            for j in range(i+1,i+groupSize):
                if j == len(keys) or keys[j] != keys[j-1] + 1 or counter[keys[j]] < init_count: return False
                counter[keys[j]] -= init_count
                # count removal
                count -= init_count
        return count == 0
