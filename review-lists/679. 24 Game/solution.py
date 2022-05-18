class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        self.res = False
        self.helper(cards)
        return self.res
    
    def helper(self, cards):
        if self.res: return
        if len(cards) == 1:
            if abs(cards[0] - 24.0) < 0.001:
                self.res = True
            return
        for i in range(len(cards)):
            for j in range(i):
                p1 = cards[i]
                p2 = cards[j]
                next = [p1 + p2, p1 - p2, p2 - p1, p1 * p2]
                if abs(p1) > 0.001:
                    next.append(p2 / p1)
                if abs(p2) > 0.001:
                    next.append(p1 / p2)
                cards.pop(i)
                cards.pop(j)
                for num in next:
                    cards.append(num)
                    self.helper(cards)
                    cards.pop()
                cards.insert(j, p2)
                cards.insert(i, p1)
        
