class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generateParenthesisHelper(res,'',0,0,n)
        return res
    
    def generateParenthesisHelper(self,res,cur,open_par,close_par,max_num):
        if len(cur) == 2*max_num:
            res.append(cur)
            return
        if open_par < max_num:
            self.generateParenthesisHelper(res,cur+'(',open_par+1,close_par,max_num)
        if close_par < open_par:
            self.generateParenthesisHelper(res,cur+')',open_par,close_par+1,max_num)
