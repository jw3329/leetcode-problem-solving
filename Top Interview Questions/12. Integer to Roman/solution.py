class Solution:
    def intToRoman(self, num: int) -> str:
        romannum_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        sorted_key = sorted(romannum_dict.keys(),reverse=True)
        res = ''
        while num != 0:
            for key in sorted_key:
                if key <= num:
                    num -= key
                    res += romannum_dict[key]
                    break
        return res
