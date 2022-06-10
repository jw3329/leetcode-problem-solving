class Solution:
    def reorderSpaces(self, text: str) -> str:
        # count number of spaces
        # count number of words
        # divide by words - 1 and rest put it into end
        word = ''
        spaces = 0
        words = []
        for c in text:
            if c == ' ':
                if word != '':
                    words.append(word)
                spaces += 1
                word = ''
            else:
                word += c
        if word != '': words.append(word)
        if len(words) == 1: return words[0] + ' ' * spaces
        each = spaces // (len(words) - 1)
        end = spaces % (len(words) - 1)
        return (' ' * each).join(words) + ' ' * end
