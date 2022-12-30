class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # bfs
        queue = deque([startGene])
        level = 0
        visited = set()
        chars = 'ACGT'
        bank_set = set(bank)
        if endGene not in bank_set: return -1
        while queue:
            level += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr in visited: continue
                visited.add(curr)
                for i in range(len(curr)):
                    for c in chars:
                        new_str = curr[:i] + c + curr[i+1:]
                        if new_str == endGene: return level
                        if new_str in bank_set:
                            queue.append(new_str)
        return -1
