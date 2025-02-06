# Let's say we have a graph of tasks to run:

# 1 -> 3 -> 5 -> 8
#      |         ^
#      v         |
                #v
# 2 -> 4 -> 6 -> 7

# Where each task is identified by a single, unique number.

# We would like to run tasks in an "appropriate" sequential order, with the requirement that a task's dependencies should run before the task itself.

# Here are a couple appropriate orders for the example graph above:
# - 1, 2, 3, 4, 5, 6, 7, 8
# - 2, 1, 3, 4, 6, 7, 5, 8

# Implement an algorithm to output the tasks in any appropriate sequential order. You may design the input shape for the graph however you see fit.

# Now, let's assume each task has the ability to output a single integer value. We would like to implement the ability to conditionally execute tasks based on the output.

# 1 -> 3 -> 5 -> 8
#      |         ^
#      v         |
# 2 -> 4 -> 6 -> 7

# Here’s an example:
# If output of node 3 is 0, traverse the 3->4 edge.
# Otherwise, traverse the 3->5 edge.

# What would the output task list look like if
# - only the 3->4 edge was traversed?
# - only the 3->5 edge was traversed?

# Design an interface that can capture the requirements of the conditional behavior, and adapt your algorithm accordingly.



# indegree 0 -> 1,2
# 4 -> 0
# 5 -> 0
# queue []
# res [1,2,3,4,5,6,7,8]
# 

graph = {
    1: [3],
    2: [4],
    3: [4,5],
    4: [6],
    5: [8],
    6: [7],
    7: [8],
    8: []
}

conditional_path = {
    3:[4],
}

import collections

# fn (node) -> int

def solve(graph, fn):

    # refined_graph = ...

    # calculate indegrees for each node
    indegrees = dict()
    for node in graph:
        for adj in graph[node]:
            if adj not in indegrees:
                indegrees[adj] = 0
            indegrees[adj] += 1
    # indegrees
    # print(indegrees)
    # search by 0 indegrees
    queue = collections.deque([])
    for node in graph:
        # if node not in indegrees, then append to queue
        if node not in indegrees:
            queue.append(node)
    if len(queue) == 0:
        raise Exception('no root node to execute')
    # do bfs
    res = []
    # 1 -> 3 -> 4 -> 5 -> 6 -> 3
    while queue:
        node = queue.popleft()
        res.append(node)
        # search for adj
        for adj in graph[node]:
            # decrement it
            indegrees[adj] -= 1
            # check now
            if indegrees[adj] == 0:
                queue.append(adj)
    non_executed = set(graph) - set(res)
    if len(non_executed) > 0:
        print('non_executed nodes:', non_executed)
    return res


print(solve(graph))
