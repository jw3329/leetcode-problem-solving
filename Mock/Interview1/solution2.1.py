class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        count1,count2,cand1,cand2 = 0,0,0,1
        
        for num in nums:
            if num == cand1: count1 += 1
            elif num == cand2: count2 += 1
            elif count1 == 0: cand1, count1 = num, 1
            elif count2 == 0: cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        return [res for res in (cand1,cand2) if nums.count(res) > len(nums) // 3]
