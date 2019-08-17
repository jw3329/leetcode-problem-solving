class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0] * 26
        max_val = 0
        max_count = 0
        for task in tasks:
            index = ord(task) - ord('A')
            counter[index] += 1
            if counter[index] == max_val:
                max_count += 1
            elif counter[index] > max_val:
                max_val = counter[index]
                max_count = 1
                
        part_count = max_val - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_val * max_count
        idles = max(0,empty_slots - available_tasks)
        return len(tasks) + idles
