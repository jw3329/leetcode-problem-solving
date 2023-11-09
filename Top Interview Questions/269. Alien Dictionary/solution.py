from typing import (
    List,
)

import heapq

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        # t < f
        # w < e
        # r < t
        # e < rf
        # w < e < r < t < f
        # create map, key for former, value for latter
        # grab all information 
        # then we will have list of chars
        # make separate graph of degree, pointing
        # from indegree of 0, do bfs, then if indegree is 0, then append to queue
        # for all string generated, return

        def generate(word1, word2):
            # check each index by index
            # iterate c and put into all chars
            i = 0
            while i < len(word1) and i < len(word2):
                if word1[i] != word2[i]:
                    # then it means, word1 has less lexicographical order
                    c_map[word1[i]].add(word2[i])
                    return True
                i += 1
            if i < len(word1): return False
            return True

        # generate key map
        c_map = dict()

        # init c_map vertex
        for word in words:
            for c in word:
                c_map[c] = set()

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # mark into c_map
                if not generate(words[i], words[j]): return ''
        
        # now we set up indegree
        degree_map = dict()
        for c in c_map:
            if c not in degree_map:
                degree_map[c] = 0
            # iterate and increment
            for d in c_map[c]:
                if d not in degree_map:
                    degree_map[d] = 0
                # increment
                degree_map[d] += 1
        # now find all 0 degree, and put into queue
        queue = []
        for c in degree_map:
            if degree_map[c] == 0:
                heapq.heappush(queue, c)
        # now setup completes
        res = ''
        while queue:
            popped = heapq.heappop(queue)
            res += popped
            # remove from all chars
            # iterate all c_map and decrement degree_map
            if popped not in c_map: continue
            for v in c_map[popped]:
                # decrement degree map
                degree_map[v] -= 1
                if degree_map[v] == 0:
                    # append to queue
                    heapq.heappush(queue, v)
        # iterate all chars, 
        # b should come before d
        return res if len(res) == len(c_map) else ''
        
