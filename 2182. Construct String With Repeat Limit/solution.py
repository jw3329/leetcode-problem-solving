class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # get count
        # priority queue, char, freq, pop, then decremenet by repeat limit, then repush
        # do until empty
        counter = collections.Counter(s)
        heap = []
        for key in counter:
            heapq.heappush(heap, (-ord(key), key, counter[key]))
        res = ''
        while heap:
            c_ord, c, count = heapq.heappop(heap)
            if count <= repeatLimit:
                res += c * count
            else:
                res += c * repeatLimit
                if heap:
                    c2_ord, c2, count2 = heapq.heappop(heap)
                    heapq.heappush(heap, (c_ord, c, count - repeatLimit))
                    res += c2
                    if count2 > 1:
                        heapq.heappush(heap, (c2_ord, c2, count2 - 1))
                else:
                    return res
        return res
