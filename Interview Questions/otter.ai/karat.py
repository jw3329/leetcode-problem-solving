"""
We are building a word processor and we would like to implement a "reflow" functionality that also applies full justification to the text.

Given an array containing lines of text and a new maximum width, re-flow the text to fit the new width. Each line should have the exact specified width. If any line is too short, insert '-' (as stand-ins for spaces) between words as equally as possible until it fits.

Note: we are using '-' instead of spaces between words to make testing and visual verification of the results easier.


lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]

reflowAndJustify(lines, 24) "reflow lines and justify to length 24" =>

        [ "The--day--began-as-still",
          "as--the--night--abruptly",
          "lighted--with--brilliant",
          "flame" ] // <--- a single word on a line is not padded with spaces

reflowAndJustify(lines, 25) "reflow lines and justify to length 25" =>

        [ "The-day-began-as-still-as"
          "the-----night----abruptly"
          "lighted---with--brilliant"
          "flame" ]

reflowAndJustify(lines, 26) "reflow lines and justify to length 26" =>

        [ "The--day-began-as-still-as",
          "the-night-abruptly-lighted",
          "with----brilliant----flame" ]

reflowAndJustify(lines, 40) "reflow lines and justify to length 40" =>

        [ "The--day--began--as--still--as-the-night",
          "abruptly--lighted--with--brilliant-flame" ]

reflowAndJustify(lines, 14) "reflow lines and justify to length 14" =>

        ['The--day-began',
         'as---still--as',
         'the------night',
         'abruptly',
         'lighted---with',
         'brilliant',
         'flame']

reflowAndJustify(lines, 15) "reflow lines and justify to length 15" =>

        ['The--day--began',
         'as-still-as-the',
         'night--abruptly',
         'lighted----with',
         'brilliant-flame']

lines2 = [ "a b", "c d" ]         

reflowAndJustify(lines2, 20) "reflow lines2 and justify to length 20" =>

        ['a------b-----c-----d']

reflowAndJustify(lines2, 4) "reflow lines2 and justify to length 4" =>

        ['a--b',
         'c--d']

reflowAndJustify(lines2, 2) "reflow lines2 and justify to length 2" =>

        ['a',
         'b',
         'c',
         'd']

All Test Cases:
                 lines, reflow width
reflowAndJustify(lines, 24)
reflowAndJustify(lines, 25)
reflowAndJustify(lines, 26)
reflowAndJustify(lines, 40)
reflowAndJustify(lines, 14)
reflowAndJustify(lines, 15)
reflowAndJustify(lines2, 20)
reflowAndJustify(lines2, 4)
reflowAndJustify(lines2, 2)

n = number of words OR total characters
"""




# words1 = [ "The", "day", "began", "as", "still", "as", "the",
#           "night", "abruptly", "lighted", "with", "brilliant",
#           "flame" ]

# wrapLines(words1, 13) "wrap words1 to line length 13" =>

#   [ "The-day-began",
#     "as-still-as",
#     "the-night",
#     "abruptly",
#     "lighted-with",
#     "brilliant",
#     "flame" ]

def wrapLines(words, num):
    # iterate words
    res = []
    temp = []
    for word in words:
        # try appending to temp
        temp.append(word)
        # do join with -
        trial = '-'.join(temp)
        # check if trial is less than num or not
        # if less, then we keep going with temp
        # if not, then pop, then append existing one
        if len(trial) > num:
            temp.pop()
            res.append('-'.join(temp))
            temp = [word]
    if temp:
        res.append('-'.join(temp))
    return res
        

lines = ["The day began as still as the","night abruptly lighted with","brilliant flame"]
lines2 = ["a b","c d"]

# n -> len(words)
# k -> worst of len(words[0])

# time: o(n)
# space: o(n)


def fill(temp, num):
    if len(temp) == 1:
        return temp[0]
    # check dash availability first
    # start from 1 dash
    # do until we find it's more
    # if it's fit, then just return
    # The day began as still
    # 24
    # The--day--began-as-still -> 24
    # The-day-began-as-still -> 22
    # The--day--began--as--still -> 26
    # target is 24
    # we are having extra 2 for double dash
    # then we can find, 2
    # do prev dash first
    # and append additionally evenly from start, to make overall number
    trial = 1
    while len(('-'*trial).join(temp)) < num:
        trial += 1
    # if it's even or more, then breaks
    # check even point
    if len(('-'*trial).join(temp)) == num: return ('-'*trial).join(temp)
    # now it means trial length is more than number
    # we do trial - 1 then join
    # it's more onto
    # we do excess - num to do join as trial, and rest to trial - 1
    excess = len(('-'*trial).join(temp))
    diff = excess - num
    res = ''
    count = 0
    for i in range(len(temp)):
        # do append
        res += temp[i]
        if i < len(temp) - 1:
            if count < diff:
                count += 1
                res += '-'*trial
            else:
                res += '-'*(trial-1)
    return res

def reflowAndJustify(lines, num):
    # iterate words
    res = []
    temp = []
    # lines to words first
    words = []
    for line in lines:
        words += line.split(' ')
    
    
    
    for word in words:
        # try appending to temp
        temp.append(word)
        # do join with -
        trial = '-'.join(temp)
        # if it exact match
        # if less
        # if more
        # if exact match, then just put into res
        # if less, then keep going
        # if more, then pop, then refine string, then put into res
        if len(trial) == num:
            res.append(trial)
            temp = []
        elif len(trial) > num:
            temp.pop()
            res.append(fill(temp, num))
            temp = [word]
    if temp:
        res.append(fill(temp, num))
    return res

print(reflowAndJustify(lines, 24))
print(reflowAndJustify(lines, 25))
print(reflowAndJustify(lines, 26))
print(reflowAndJustify(lines, 40))
print(reflowAndJustify(lines, 14))
print(reflowAndJustify(lines, 15))
print(reflowAndJustify(lines2, 20))
print(reflowAndJustify(lines2, 4))
print(reflowAndJustify(lines2, 2))
