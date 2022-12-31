class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # map index of task type
        # if met, check diff of space
        res = 0
        index_map = dict()
        # keeps track of day of the task
        day = 0
        for task in tasks:
            if task not in index_map:
                index_map[task] = day
            else:
                between_days = day - index_map[task] - 1
                if between_days < space:
                    day += space - between_days
                index_map[task] = day
            day += 1
        return day
