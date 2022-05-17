class Solution:
    def arrangeWords(self, text: str) -> str:
        # split first,
        # in heap, (-len, index, text)
        # join with space, then upper first
        splitted = text.split(' ')
        heap = []
        for i, word in enumerate(splitted):
            heapq.heappush(heap, (len(word), i, word.lower()))
        res = ''
        n = len(heap)
        for i in range(n):
            _, _, word = heapq.heappop(heap)
            if i == 0:
                word = word[0].upper() + word[1:]
            res += word
            if i != n - 1:
                res += ' '
        return res
