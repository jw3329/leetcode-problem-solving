class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        str_list = []
        filtered_str = ''
        for c in paragraph:
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                filtered_str += c.lower()
            else:
                if filtered_str: str_list.append(filtered_str)
                filtered_str = ''
        if filtered_str: str_list.append(filtered_str)
        
        counter = collections.Counter(str_list)
        
        for word in banned:
            if word in counter: counter.pop(word)
        
        max_val = -1
        max_key = ''
        for key,value in counter.items():
            if max_val < value:
                max_val = value
                max_key = key
        return max_key
