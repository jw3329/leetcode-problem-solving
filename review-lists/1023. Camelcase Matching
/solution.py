class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            # set up query index and pattern index
            query_i = 0
            pattern_i = 0
            val = True
            while query_i < len(query) and pattern_i < len(pattern):
                # upper, upper
                # lower, lower
                # lower, none
                if query[query_i] == pattern[pattern_i]:
                    query_i += 1
                    pattern_i += 1
                elif 'a' <= query[query_i] <= 'z':
                    query_i += 1
                else:
                    val = False
                    break
            # check when query left, it should only contain lower case
            while query_i < len(query):
                if 'A' <= query[query_i] <= 'Z':
                    val = False
                    break
                else:
                    query_i += 1
            
            # if we have pattern i left with non query, we make it false
            if pattern_i != len(pattern):
                val = False
            res.append(val)
        return res
