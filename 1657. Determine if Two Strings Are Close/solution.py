class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # you can make infinite swap, so operation 1 doesn't matter
        # try to count number of frequency of word1, then check the values, if values are identical with word2 values, then operation2 can be achived
        # we have 
        # a -> 3, b -> 2, c -> 1
        # b -> 3, a -> 2, c -> 1
        
        # swapping two key should match with second map
        # try swapping, one by one, if match with second, mark those as visited, do rest of dfs
        counter1 = collections.Counter(word1)
        counter2 = collections.Counter(word2)
        return set(counter1) == set(counter2) and sorted(counter1.values()) == sorted(counter2.values())
