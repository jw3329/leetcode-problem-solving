class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split(' ')
        res = []
        for word in splitted:
            res.append(word[::-1])
        return ' '.join(res)
