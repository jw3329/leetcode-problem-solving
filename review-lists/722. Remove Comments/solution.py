class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        open = False
        string = ''
        res = []
        for line in source:
            i = 0
            while i < len(line):
                if open:
                    if line[i] == '*' and i + 1 < len(line) and line[i+1] == '/':
                        open = False
                        i += 1
                else:
                    if line[i] == '/' and i + 1 < len(line) and line[i+1] == '/':
                        break
                    elif line[i] == '/' and i + 1 < len(line) and line[i+1] == '*':
                        open = True
                        i += 1
                    else:
                        string += line[i]
                i += 1
            if not open and len(string) > 0:
                res.append(string)
                string = ''
        return res
