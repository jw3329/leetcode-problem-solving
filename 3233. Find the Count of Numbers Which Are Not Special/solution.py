class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        # 1 2 4 8
        # only things it's prime number squared is special
        # get all special numbers, then we find how many special numbers are in the list
        # then we subtract the amount
        # since it's too big, find all primes, then check with squared value
        primes = []
        i = 0
        while i * i <= r: 
            primes.append(True)
            i += 1
        i = 2
        while i * i <= r:
            j = 2
            while i * j < len(primes):
                primes[i*j] = False
                j += 1
            i += 1
        # now all primes with true is prime
        # check availability
        count = 0
        i = 2
        while i * i <= r:
            if not primes[i]: 
                i += 1
                continue
            # make square of it
            squared = i * i
            if squared >= l:
                count += 1
            i += 1
        # 3 5
        # 9 25
        # 20 - ()
        return r - l + 1 - count
