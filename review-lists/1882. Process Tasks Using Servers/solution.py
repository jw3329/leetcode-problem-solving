class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # we build priority queue,
        # (server weight, index)
        # track current time
        # put end time into heap, 
        res = []
        # put into queue
        free = []
        used = []
        for i in range(len(servers)):
            heapq.heappush(free, (servers[i], i))
        for i in range(len(tasks)):
            # pop used if we have task to free
            while used and used[0][0] <= i:
                _, server, index = heapq.heappop(used)
                heapq.heappush(free, (server, index))
            
            # if we have server to put, put into it
            if free:
                server, index = heapq.heappop(free)
                heapq.heappush(used, (i + tasks[i], server, index))
                res.append(index)
            else:
                # if no free, then we pop used one, then append, then reinsert with updated time
                time, server, index = heapq.heappop(used)
                res.append(index)
                heapq.heappush(used, (time + tasks[i], server, index))
        return res
