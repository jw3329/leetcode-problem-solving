class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.order_map = {c:i for i,c in enumerate(order)}
        for i in range(1,len(words)):
            word1 = words[i-1]
            word2 = words[i]
            
            if not self.is_smaller(word1,word2): return False
        return True
    
    def is_smaller(self,word1,word2):
        i = 0
        while i < min(len(word1),len(word2)):
            if self.order_map[word1[i]] < self.order_map[word2[i]]: return True
            elif self.order_map[word1[i]] > self.order_map[word2[i]]: return False
            i += 1
        return i == len(word1)
