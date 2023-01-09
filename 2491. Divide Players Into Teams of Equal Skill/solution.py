class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # sort, then first and last, check, then add product
        skill.sort()
        val = skill[0] + skill[-1]
        res = skill[0] * skill[-1]
        for i in range(1,len(skill) // 2):
            if val != skill[i] + skill[len(skill)-1-i]: return -1
            res += skill[i] * skill[len(skill)-1-i]
        return res
