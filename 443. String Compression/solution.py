class Solution:
    def compress(self, chars: List[str]) -> int:
        # curr char
        # number
        # if number is > 1, then increment count, else no
        curr = chars[0]
        num = 1
        index = 1
        for i in range(1, len(chars)):
            c = chars[i]
            # if c is same with curr, then increment number
            if c == curr:
                # check if curr num is equal to 1
                num += 1
            else:
                # append curr so far number to index
                if num > 1:
                    str_num = str(num)
                    for c2 in str_num:
                        chars[index] = c2
                        index += 1
                # change curr and increment
                curr = c
                num = 1
                # also put curr char to chars
                chars[index] = curr
                index += 1
        # check if num is bigger, then append
        if num > 1:
            str_num = str(num)
            for c in str_num:
                chars[index] = c
                index += 1
        return index
