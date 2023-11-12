class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        # sliding window problem
        if k == 0: return 0
        left = right = 0
        char_map = dict()
        count = 0
        res = 0
        while right < len(s):
            # append if available
            if s[right] not in char_map:
                char_map[s[right]] = 0
            if char_map[s[right]] == 0:
                count += 1
            char_map[s[right]] += 1
            # check now
            while left < right and count > k:
                # do same operation for left
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    count -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
