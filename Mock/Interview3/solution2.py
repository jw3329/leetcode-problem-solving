class Solution:
    
    def __init__(self):
        self.dict = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        if len(digits) == 1: return list(self.dict[digits[0]])
        prev_comb = self.letterCombinations(digits[1:])
        res = []
        for c in self.dict[digits[0]]:
            for prev_str in prev_comb:
                res.append(c + prev_str)
        return res
