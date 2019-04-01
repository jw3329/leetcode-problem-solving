class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        res = ''
        i = 0
        while i < len(strs[0]):
            letter = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != letter:
                    return res
            res += letter
            i += 1
        return res
                
