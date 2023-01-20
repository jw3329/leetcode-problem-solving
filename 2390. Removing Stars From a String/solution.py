class Solution:
    def removeStars(self, s: str) -> str:
        # star finding, pop left non star,
        stack = []
        delete_index = set()
        for i, c in enumerate(s):
            if c != '*':
                stack.append(i)
            else:
                # when star, mark both to delete index
                delete_index.add(i)
                if stack:
                    delete_index.add(stack.pop())
        res = []
        for i, c in enumerate(s):
            if i not in delete_index:
                res.append(c)
        return ''.join(res)
