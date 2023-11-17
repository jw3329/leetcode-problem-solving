# Given a list of city names and their corresponding populations, 
# write a program with a parameterless method to output a random city name 
# subject to the following constraint: 
# the probability of the function to output a city's name is based on 
# its population divided by the sum of all cities' population. 
# Assume the program will be repeatedly called many times.

# For example:
# - NY: 7000000
# - SF: 5000000
# - LA: 8000000

# The probability to generate NY is 7/20, SF is 1/4

# sum will be 20M
# each city has their population
# we make random integer generation from
# 1 to 20M
# for the integer within the range of city will be returned
# [5M, 12M, 20M] -> sorted order
# generate integer, 
# binary search for existing city that has been ordered, we can have appropriate range, then we make return for that city

import random

class City:


    def __init__(self, values):
        # dict will be like 
        # n cities
        # - NY: 7000000
        # - SF: 5000000
        # - LA: 8000000
        # make up prefix sum of each
        # [(NY, 7M), (SF, 12M), (LA, 20M)]
        self.prefix = [] # Time: O(n), Space: O(n)
        self.total = 0
        for key, value in values.items():
            self.total += value
            self.prefix.append((key, self.total))
        # prefix -> [(NY, 7M), (SF, 12M), (LA, 20M)]
        
    def generate(self):
        # check if prefix exist
        if not self.prefix: raise Exception('No cities to generate')
        # generate random integer
        # 1~7M -> NY, 7M1 ~ 12M -> SF, 12M1 -> 20M -> LA
        rand_int = random.randint(1, total) # 8M503 # O(1)
        # we have to find which boundary this integer belongs to
        left = 0
        right = len(self.prefix) - 1 # 2
        # binary search for rand_int
        while left < right: # O(logN)
            mid = left + (right - left) // 2 # 0
            # make comparison
            # if mid value is less than rand_int, then search right -> left = mid + 1
            # if other, then search left -> right = mid
            if self.prefix[mid][1] < rand_int:
                left = mid + 1 # 1
            else:
                right = mid # 1
        # we've got the value
        return self.prefix[left][0] # SF # Time: O(logN), Space: O(1)






# Given an array of integers and a window size, return an array with the average of each window within the array

# Example: [1,2,3,4,5,6,7,8,9] and window size = 7

# Result: [4.0,5.0,6.0]

# Further Explanation:
# AVG([1,2,3,4,5,6,7]) => 4.0 (28/7)
# AVG([2,3,4,5,6,7,8]) => 5.0 (35/7)
# AVG([3,4,5,6,7,8,9]) => 6.0 (42/7)

# add up first 7 elements, we are putting it into first return [4.0]
# we are having 7 elements summed up, as we iterate, we can add up new element, and subtract first element, then we make another average
# we keep going, then return


def AVG(arr, size):
    if size > len(arr): raise Exception('size is more than length of arr')
    # first add up first size of element
    res = []
    curr = 0
    while self.i < len(arr):
        curr += arr[i]
        # check if i >= size - 1
        # if not, then just continue
        # if it is, then make average, then return
        if i >= size - 1:
            # check if things to be subtracted
            if i >= size:
                curr -= arr[i-size]
            # make average, then put into res
            res.append(curr / size)
    return res


AVG([1,2,3,4,5,6,7,8,9], 7)
AVG([], 0)
AVG([1,2,3,4,5,6,7,8,9], 10) # n -> length of arr, k -> size
# Runtime : O(n)
# Space: O(n - k)
# i to be current iteration point, increment prev defined i and then make up averages
