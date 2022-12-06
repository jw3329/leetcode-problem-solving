class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        splitted = text.split(' ')
        broken_set = set(brokenLetters)
        res = 0
        for word in splitted:
            is_fine = True
            for c in word:
                if c in broken_set:
                    is_fine = False
                    break
            if is_fine:
                res += 1
        return res
            
