class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set: return 0
        head = set() 
        tail = set()
        
        head.add(beginWord)
        tail.add(endWord)
        
        ladder = 2
        while head and tail:
            if len(head) >= len(tail):
                temp = head
                head = tail
                tail = temp
            temp = set()
            for word in head:
                for i in range(len(word)):
                    for c in range(ord('a'),ord('z')+1):
                        c = chr(c)
                        check_word = word[:i] + c + word[i+1:]
                        if check_word in tail:
                            return ladder
                        if check_word in word_set:
                            temp.add(check_word)
                            word_set.remove(check_word)
            ladder += 1
            head = temp
        return 0
                    