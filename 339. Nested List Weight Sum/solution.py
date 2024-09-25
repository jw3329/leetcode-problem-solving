def helper(elem, depth):
    res = 0
    for elem2 in elem:
        if type(elem2) == int:
            res += elem2 * depth
        else:
            res += helper(elem2, depth + 1)
    return res


def solve(input):
    return helper(input, 1)


input = [[1, 1], 2, [1, 1]]

print(solve(input))

input = [1, [4, [6]]]

print(solve(input))
