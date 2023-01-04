class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        # check number divisible by p
        # 10011 -> at most k 1 should be present in subarray
        # curr number of subarray is, prev number of subarray + if we count curr number
        # not divisible -> prev + prev + 1, same for divisible, but count < k, sliding window?
        res = set()
        for i in range(len(nums)):
            count = 0
            temp = []
            for j in range(i, len(nums)):
                temp.append(nums[j])
                if nums[j] % p == 0:
                    count += 1
                if count > k: break
                res.add(tuple(temp))
        return len(res)
