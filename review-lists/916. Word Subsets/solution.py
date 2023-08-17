class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def count(s):
            res = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                res[i] += 1
            return res
        
        max_count = [0] * 26
        for word in words2:
            counter = count(word)
            # grab maximum
            for i in range(26):
                max_count[i] = max(max_count[i], counter[i])
        res = []
        for word in words1:
            # grab counter of word
            counter = count(word)
            # compare
            failed = False
            for i in range(26):
                if counter[i] < max_count[i]:
                    failed = True
                    break
            if not failed:
                res.append(word)
        return res
