class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needed = collections.Counter(p)
        count = len(p)
        left = 0
        right = 0
        res = []
        while right < len(s):
            if needed[s[right]] >= 1:
                count -= 1         
            needed[s[right]] -= 1
            right += 1
            if count == 0: res.append(left)
            
            if right - left == len(p):
                if needed[s[left]] >= 0:
                    count += 1  
                needed[s[left]] += 1
                left += 1
        return res
