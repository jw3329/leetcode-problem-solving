class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        index_set = set()
        index_list = []
        while len(index_set) < len(self.nums):
            index = random.randint(0,len(self.nums) - 1)
            if index not in index_set: 
                index_set.add(index)
                index_list.append(index)
        
        return [self.nums[i] for i in index_list]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
