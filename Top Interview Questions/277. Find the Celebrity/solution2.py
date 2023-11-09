"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        cand = 0
        # check cand if it knows somebody,
        # try to filter the candidate by iterating
        for i in range(1, n):
            if Celebrity.knows(cand, i):
                # if candidate knows, then it means it's not candidate, reset to known
                cand = i
        # now we have last candidate
        # check if this candidate doesn't know all
        if any(Celebrity.knows(cand, i) for i in range(cand)): return -1
        if any(not Celebrity.knows(i, cand) for i in range(n)): return -1
        return cand
