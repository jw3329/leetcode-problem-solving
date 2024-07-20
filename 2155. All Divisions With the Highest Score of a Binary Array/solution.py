class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # track
        # left score, right score
        # if 1, then -1
        # if 0, then +1
        # if max, then make it new
        # if same, then append
        res = [0]
        # get num of 1 first
        counter = collections.Counter(nums)
        curr_val = counter.get(1, 0)
        max_val = curr_val
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_val -= 1
            else:
                curr_val += 1
            if curr_val > max_val:
                max_val = curr_val
                res = [i+1]
            elif curr_val == max_val:
                res.append(i+1)
        return res
            
