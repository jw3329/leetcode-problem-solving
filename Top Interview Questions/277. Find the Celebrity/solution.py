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
        if n == 1: return 0
        # Write your code here
        # we have people id of 0 to n-1
        known_map = dict()
        for i in range(n):
            if i not in known_map:
                known_map[i] = set()
            for j in range(n):
                if i == j: continue
                if Celebrity.knows(i, j):
                    known_map[i].add(j)
        # now find indegree
        indegree = dict()
        for i in known_map:
            for j in known_map[i]:
                if j not in indegree:
                    indegree[j] = 0
                indegree[j] += 1
        # now iterate indegree which has n - 1 known people, and check if known for that person is none
        for i in indegree:
            if indegree[i] == n - 1:
                # check known for that
                if len(known_map[i]) == 0: return i
        return -1
