class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            no_anagram = True
            keyword = ''.join(sorted(s))
            if keyword in anagram_dict:
                anagram_dict[keyword].append(s)
            else:
                anagram_dict[keyword] = [s]
        res = []
        for key in anagram_dict:
            res.append(anagram_dict[key])
        return res
