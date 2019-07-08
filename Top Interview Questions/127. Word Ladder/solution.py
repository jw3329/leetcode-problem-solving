class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        todo = [beginWord]
        word_dict = set(wordList)
        ladder = 1
        while todo:
            for i in range(len(todo)):
                word = todo.pop(0)
                if word == endWord: return ladder
                if word in word_dict: word_dict.remove(word)
                for j in range(len(word)):
                    for k in range(0,26):
                        trial = chr(ord('a') + k)
                        temp_word = word[:j] + trial + word[j+1:]
                        if temp_word in word_dict:
                            todo.append(temp_word)
            ladder += 1
        return 0
