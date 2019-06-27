class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.strip().split()
        return ' '.join(word_list[::-1])
