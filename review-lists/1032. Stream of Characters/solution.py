def index(c):
    return ord(c) - ord('a')

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.word = False
        

def build_trie(words):
    root = Trie()
    for word in words:
        curr = root
        for c in word[::-1]:
            i = index(c)
            if not curr.children[i]:
                curr.children[i] = Trie()
            curr = curr.children[i]
        curr.word = True
    return root
        
class StreamChecker:

    def __init__(self, words: List[str]):
        # build trie, from backward, 
        # check if contains, if contains, true, else false
        self.root = build_trie(words)
        self.curr = ''

    def query(self, letter: str) -> bool:
        # append one by one, check if curr in words, iterate backward, if matche, true
        # trie for d, c
        self.curr += letter
        curr_trie = self.root
        for i in range(len(self.curr)-1, -1, -1):
            c = self.curr[i]
            # join one by one
            c_index = index(c)
            curr_trie = curr_trie.children[c_index]
            if not curr_trie: return False
            # check if it's word
            if curr_trie.word: return True
        return False
        
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
