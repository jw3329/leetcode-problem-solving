class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        # iterate, target will increment as index of node
        score = [0] * n
        max_val = 0
        max_node = n
        for i in range(n):
            score[edges[i]] += i
            if max_val < score[edges[i]]:
                max_val = score[edges[i]]
                max_node = edges[i]
            elif max_val == score[edges[i]]:
                max_node = min(max_node, edges[i])
        return max_node
