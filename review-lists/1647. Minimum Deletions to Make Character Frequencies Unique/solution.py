class Solution:
    def minDeletions(self, s: str) -> int:
        # all frequency should be diff
        # if you put into bracket, then you will have individual
        # array with index, how to make all 1 or 0 is the problem
        # move to left
        # put into stack, where it has not filled, which is empty
        counter = collections.Counter(s)
        # put into counter index
        index = [0] * 100000
        # put the counter into index
        # we are having 0 based index
        for c in counter:
            index[counter[c] - 1] += 1
        stack = []
        res = 0
        # a:3 b:2 c:2 e:1
        # 1 2 1
        for i in range(len(index)):
            if index[i] == 0:
                stack.append(i)
            else:
                # place existing number until it's 1
                while index[i] > 1:
                    # pop and place into stack place
                    if stack:
                        popped = stack.pop()
                        res += i - popped
                    else:
                        res += i + 1
                    index[i] -= 1
        return res
