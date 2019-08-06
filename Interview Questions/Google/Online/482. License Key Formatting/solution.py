class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        filtered_str = ''.join(S.split('-'))
        reversed_list = []
        temp_str = ''
        for c in filtered_str[::-1]:
            if len(temp_str) < K:
                temp_str += c.upper()
            else:
                reversed_list.append(temp_str[::-1])
                temp_str = c.upper()
        if temp_str: reversed_list.append(temp_str[::-1])
        return '-'.join(reversed_list[::-1])

