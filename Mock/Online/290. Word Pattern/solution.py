class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        splitted = str.split(' ')
        if len(pattern) != len(splitted): return False
        map = {}
        word_set = set()
        for i in range(len(pattern)):
            if pattern[i] not in map and splitted[i] not in word_set:
                map[pattern[i]] = splitted[i]
                word_set.add(splitted[i])
            else:
                if pattern[i] not in map or map[pattern[i]] != splitted[i]: return False
        return True
