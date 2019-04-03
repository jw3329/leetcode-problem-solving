class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int dup_count = 0;
        int swap_index = 1;
        for(int i=1;i<nums.size();i++) {
            if(nums[i] == nums[i-1]) dup_count++;
            else {
                nums[swap_index++] = nums[i];
            }
        }
        return nums.size() - dup_count;
    }
};
