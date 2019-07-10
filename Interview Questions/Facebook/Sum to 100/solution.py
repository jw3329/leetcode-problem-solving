class Solution:
    
    def sum_to_100(self, s):
        combinations = self.get_all_combinations(s)
        res = []
        #self.sum_to_k(combinations,res,100,'')
        for comb in combinations:
            self.sum_to_k(comb,res,100,'')

        for i in range(len(res)):
            if res[i][0] == '+':
                res[i] = res[i][1:]
        return res 

    def sum_to_k(self,combination,res,k,string):
        if not combination:
            if k == 0:
                res.append(string)
            return

        self.sum_to_k(combination[1:],res,k - int(combination[0]), string + f'+{combination[0]}')
        self.sum_to_k(combination[1:],res,k + int(combination[0]), string + f'-{combination[0]}')
        


    def get_all_combinations(self,s):
        if len(s) == 1: return [[s]]
        print(s)
        rest_comb = self.get_all_combinations(s[1:])
        res = []
        for comb in rest_comb:
            res.append([s[0]] + comb)
            res.append([s[0] + comb[0]] + comb[1:])

        return res




solution = Solution()

print(solution.sum_to_100('123456789'))
