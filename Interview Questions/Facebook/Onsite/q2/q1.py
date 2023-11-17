def solve(s):
    # make into list
    # do left to right
    # do right to left
    s_list = list(s)
    open = 0
    for i in range(len(s_list)):
        c = s_list[i]
        if c == "(":
            open += 1
        elif c == ")":
            if open == 0:
                s_list[i] = "#"
            else:
                open -= 1
    open = 0
    for i in range(len(s_list) - 1, -1, -1):
        c = s_list[i]
        if c == ")":
            open += 1
        elif c == "(":
            if open == 0:
                s_list[i] = "#"
            else:
                open -= 1
    return "".join(filter(lambda x: x != "#", s_list))


print(solve(")))123((("))
print(solve("()()()123()()"))
print(solve("((123()())"))
print(solve("((123()()))))))"))
print(solve("123()()))))))"))
print(solve("123()()(((((("))
