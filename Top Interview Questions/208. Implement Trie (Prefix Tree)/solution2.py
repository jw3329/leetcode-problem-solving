class TrieNode:
    
    def __init__(self,val):
        self.val = val
        self.children = [None for _ in range(26)]
        self.is_word = False
        
class Trie:
    
    def convert(self,c):
        return ord(c) - ord('a')

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(' ')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for i in range(len(word)):
            if not curr.children[self.convert(word[i])]:
                curr.children[self.convert(word[i])] = TrieNode(word[i])
            curr = curr.children[self.convert(word[i])]
        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in range(len(word)):
            curr = curr.children[self.convert(word[i])]
            if not curr: return False
        return curr.is_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for i in range(len(prefix)):
            curr = curr.children[self.convert(prefix[i])]
            if not curr: return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
