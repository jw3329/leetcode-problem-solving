class Solution:
    def solveEquation(self, equation: str) -> str:
        # split by equal
        # get coeff side of each
        # left side, and right side conversion
        # return
        
        def parse(side):
            sign = '+'
            curr = ''
            # iterate and add number on curr
            coeff = 0
            val = 0
            for c in side:
                if '0' <= c <= '9':
                    curr += c
                elif c == 'x':
                    # add to coeff, with sign
                    to_add = int(curr) if curr != '' else 1
                    if sign == '+':
                        coeff += to_add
                    else:
                        coeff -= to_add
                    curr = ''
                else:
                    to_add = int(curr) if curr != '' else 0
                    if sign == '+':
                        val += to_add
                    else:
                        val -= to_add
                    curr = ''
                    sign = c
            if curr:
                to_add = int(curr) if curr != '' else 0
                if sign == '+':
                    val += to_add
                else:
                    val -= to_add
            return coeff, val
                    
        left, right = equation.split('=')
        # left will be x coeff, right will be value
        coeff1, val1 = parse(left)
        coeff2, val2 = parse(right)
        coeff = coeff1 - coeff2
        val = val2 - val1
        if coeff == 0:
            if val == 0:
                return 'Infinite solutions'
            return 'No solution'
        return f'x={val // coeff}'
