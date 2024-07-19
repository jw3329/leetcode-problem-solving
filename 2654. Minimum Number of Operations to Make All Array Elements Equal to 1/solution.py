class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # if one, and next is not 1, then -1
        # [2, 6, 3, 4]
        # [2, 6, 1, 4]
        # [2, 6, 1, 1]
        # [2,1,1,1]
        # [1,1,1,1]
        # check if 1 is there, if there's 1, then we just len(nums) - # of 1
        # if one can find make 1, then then we return len(nums)
        # if there's no such way to make 1, then 
        
        # [3, 6, 2]
        
        # [1, 2, 2]
        # [1, 1, 2]
        # [1, 1, 1]
        
        # we need to find distance between two num that gcd is 1
        # min distance
        counter = collections.Counter(nums)
        ones = counter.get(1, 0)
        if ones: return len(nums) - ones
        res = sys.maxsize
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i+1,len(nums)):
                # check gcd of it
                g = gcd(g, nums[j])
                if g == 1: 
                    res = min(res, j - i + (len(nums) - 1))
                    break
        return res if res != sys.maxsize else -1
