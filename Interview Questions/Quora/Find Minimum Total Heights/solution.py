
class Solution:
    
    def __init__(self,lists,k,x):
        self.lists = lists
        self.k = k
        self.x = x

    def solve(self):
        
        res = [1] * self.k
        lists = self.lists.copy()
        while sum(res) < self.x:
            max_height = 0
            index = 0
            for i in range(self.k):
                height = len(lists[-1][i]) // res[i] + (len(lists[-1][i]) % res[i] != 0)
                if max_height < height:
                    max_height = height
                    index = i
            res[index] += 1

        return res
            

        


        










lists = [['facebook','google','uber','apple'],['lyft','airbnb','paypal','yelp']]

k = 4

x = 13

s = Solution(lists, k, x)

print(s.solve())
