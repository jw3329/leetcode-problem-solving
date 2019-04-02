class Solution:
    
    def __init__(self):
        self.num_dict = {
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
        rest_comb = self.letterCombinations(digits[1:])
        res = []
        for c in self.num_dict[digits[0]]:
            if rest_comb:
                for comb in rest_comb:
                    res.append(c + comb)
            else:
                res.append(c)
        return res
