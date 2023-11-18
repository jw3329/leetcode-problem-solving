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


def solve2(A, B):
    k = len(A) - 1
    i = len(A) - len(B) - 1
    j = len(B) - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            k -= 1
            i -= 1
        else:
            A[k] = B[j]
            k -= 1
            j -= 1
    while j >= 0:
        A[k] = B[j]
        k -= 1
        j -= 1
    return A


print(solve2([1, 3, 5, 7, None, None, None, None], [2, 4, 6, 8]))
