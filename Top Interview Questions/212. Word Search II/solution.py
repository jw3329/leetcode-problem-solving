class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.word = None

class Solution:

    def build_trie(self,words):
        root = TrieNode()
        for word in words:
            p = root
            for c in word:
                index = ord(c) - ord('a')
                if not p.children[index]: p.children[index] = TrieNode()
                p = p.children[index]
            p.word = word
        return root
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = self.build_trie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,i,j,root,res)
        return res
    
    def dfs(self,board,i,j,p,res):
        c = board[i][j]
        if c == '#' or not p.children[ord(c) - ord('a')]: return
        p = p.children[ord(c) - ord('a')]
        if p.word:
            print(i,j)
            res.append(p.word)
            p.word = None
        board[i][j] = '#'
        if i > 0: self.dfs(board,i-1,j,p,res)
        if j > 0: self.dfs(board,i,j-1,p,res)
        if i < len(board) - 1: self.dfs(board,i+1,j,p,res)
        if j < len(board[0]) - 1: self.dfs(board,i,j+1,p,res)
        board[i][j] = c
