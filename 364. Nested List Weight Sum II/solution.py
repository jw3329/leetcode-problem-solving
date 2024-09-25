def find_depth(elem):
    res = 1
    if type(elem) == int:
        return res
    for elem2 in elem:
        res = max(res, 1 + find_depth(elem2))
    return res


def helper(elem, max_depth):
    res = 0
    for elem2 in elem:
        if type(elem2) == int:
            res += elem2 * max_depth
        else:
            res += helper(elem2, max_depth - 1)
    return res


def solve(input):
    # get maximum depth first
    # then using helper function to track the depth, find values of it

    # get maximum depth
    max_depth = 1
    for elem in input:
        max_depth = max(max_depth, find_depth(elem))
    print(max_depth)
    return helper(input, max_depth)


input = [[1, 1], 2, [1, 1]]

print(solve(input))

input = [1, [4, [6]]]

print(solve(input))
