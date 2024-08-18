def findCelebrity(graph):

    def knows(a, b):
        return graph[a][b] == 1

    # check first one
    # if first one doesn't know someone
    # possibility of celebrity
    # all people should know first one
    # if at least one doesn't know first, then it's not celebrity
    # if first one knows someone, then first one is not celebrity
    # the one first knows are celebrity candidates

    # find someone possibly doesn't know anyone
    ans = 0
    for i in range(1, len(graph)):
        if knows(ans, i):
            ans = i
    for i in range(len(graph)):
        if ans != i:
            if knows(ans, i) or not knows(i, ans):
                return -1
    return ans


graph = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]

print(findCelebrity(graph))

graph = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]

print(findCelebrity(graph))
