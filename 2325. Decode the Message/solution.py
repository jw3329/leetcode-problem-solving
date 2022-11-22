class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # iterate key with set, putting into map
        conversion_map = dict()
        index = 0
        for c in key:
            if c == ' ' or c in conversion_map:
                continue
            conversion_map[c] = chr(ord('a') + index)
            index += 1
        # now work on conversion
        res = ''
        for c in message:
            if c not in conversion_map:
                res += c
            else:
                res += conversion_map[c]
        return res
                
