class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # count num of pattern
        # if left is smaller, iterate to right
        # if right is smaller, iterate to left
        counter = collections.Counter(text)
        left = counter.get(pattern[0], 0)
        right = counter.get(pattern[1], 0)
        if pattern[0] == pattern[1]:
            return (left + 1) * left // 2
        res = 0
        if left < right:
            text = pattern[0] + text
            for i in range(len(text)):
                if text[i] == pattern[0]:
                    res += right
                elif text[i] == pattern[1]:
                    right -= 1
        else:
            text += pattern[1]
            for i in range(len(text)-1,-1,-1):
                if text[i] == pattern[1]:
                    res += left
                elif text[i] == pattern[0]:
                    left -= 1
        return res
