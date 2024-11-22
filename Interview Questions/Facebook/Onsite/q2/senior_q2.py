#Given a sorted array of unique values from [0, 99], output missing numbers as a string, separated by comma. If there are more than 2 consecutive numbers, output the first and the last separated by hyphen.

#Example:
#Input: [2, 4, 7, 13, 20]
#Output: "0,1,3,5,6,8-12,14-19,21-99"



# [2, 4, 7, 13, 20]


def calculate(res, left_val, right_val): # ['0,1', '3', '5,6', '8-12', '14-19'], 21, 99
    # 0, 2 -> 0-2
    # 0, 1 -> 0,1
    # 0, 0 -> 0
    # 0, -1 -> ''
    if left_val > right_val: return res
    if left_val == right_val: return res + [str(left_val)] # ['0,1', '3']
    if right_val - left_val == 1: return res + [f"{left_val},{right_val}"] # ['0,1', '3', '5,6']
    return res + [f"{left_val}-{right_val}"] # ['0,1', '3', '5,6', '8-12', '14-19', '21-99']



def solve(arr):
    res = []
    res = calculate(res, 0, arr[0]-1) # ['0,1']
    for i in range(1, len(arr)):
        # compare each
        res = calculate(res, arr[i-1]+1, arr[i]-1) # ['0,1', '3']
    res = calculate(res, arr[-1]+1, 99)
    return ','.join(res) # ['0,1', '3', '5,6', '8-12', '14-19', '21-99']
    # '0,1,3,5,6,8-12,14-19,21-99'


#Given a list of city names and their corresponding populations, write a program to output a city name subject to the following constraint: the probability of the program to output a city's name is based on its population divided by the sum of all cities' population. Assume the program will be repeatedly called many times.

#For example:

# arg -> 
#NY: 7M
#SF: 5M
#LA: 8M

# NY -> 7

# SF -> 12

# LA -> 20

# check index of iteration

# random index generated, we do make determination by iterating those, 7, 12, 20


# random index -> 5, 5 < 7 -> NY

# 11 -> SF

# 13 -> LA

#The probability to generate NY is 7/20, SF is 5/20 and LA 8/20.

# 0 ~ 6 -> NY
# 7 ~ 11 -> SF
# 12 -> 19 -> LA

# call, it will place from 0 to 19
# ['NY', 'NY', ..., 'SF', 'SF', 'SF', ..., 'LA', 'LA'] -> pick random index, then return string of city

# call() -> 'NY', 'SF', 'LA'

# O(1) -> search, O(n) -> space complexity + Time complexity forming up

# set up first

args = dict(
    NY = 7,
    SF = 5,
    LA = 8,
)

# form up from args

def form_up_boundary():
    num_res = []
    city_res = []
    curr = 0
    for key ,val in args.items():
        curr += val
        num_res.append(curr)
        city_res.append(key)
    return num_res, city_res




boundary = form_up_boundary() # 7 -> 'NY', 12 -> 'SF', 20 -> 'LA', 
# ([7, 12, 20], ['NY', 'SF', 'LA'])
call()


def call():
    random_index = rand.randint(0, boundary[0][-1]-1)
    # iterate
    for i, bound in enumerate(boundary[0]):
        if random_index < bound:
            return boundary[1][i]


# O(n) when n is # of cities

# initialize boundary first
# call function

class Callable:

    def __init__(self, args):
        pass

    def call(self):
        pass


callable = Callable(args=args)

# call multiple 


for _ in range(100):
    callable.call()
