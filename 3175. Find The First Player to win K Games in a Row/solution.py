class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        i = 0
        curr = 0
        for j in range(1, len(skills)):
            if skills[i] < skills[j]:
                i = j
                curr = 0
            curr += 1
            if curr == k: break
        return i
