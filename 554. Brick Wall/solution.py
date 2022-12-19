class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # multiple for walls
        # each wall, track prefix sum, 0 1 3 5 6
        # each line putting into vertical sets trial
        # count how many edges for each verticals
        # for each vertical, track min, by total - its vertical count
        # return
        edge_freq = collections.defaultdict(int)
        max_freq = 0
        for row in range(len(wall)):
            edge_pos = 0
            for i in range(len(wall[row])-1):
                curr = wall[row][i]
                edge_pos += curr
                edge_freq[edge_pos] += 1
                max_freq = max(max_freq, edge_freq[edge_pos])
        return len(wall) - max_freq
