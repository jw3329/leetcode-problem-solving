class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for _str in strs:
            sorted_str = ''.join(sorted(_str))
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []
            anagram_map[sorted_str].append(_str)
        res = []
        for value in anagram_map.values():
            res.append(value)
        return res
